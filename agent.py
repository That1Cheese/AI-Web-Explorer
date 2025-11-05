#!/mnt/c/Users/James/Desktop/AI Web Explorer/venv/bin/python3
"""
AI Agent - Combines web search and LLM
Decides when to search, retrieves info, and generates summaries
"""

import os
import sys
import requests
from dotenv import load_dotenv
import google.generativeai as genai

# Load credentials
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def web_search(query, num_results=5):
    """Search Google and return results"""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': GOOGLE_API_KEY,
        'cx': GOOGLE_SEARCH_ENGINE_ID,
        'q': query,
        'num': num_results
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        results = []
        if 'items' in data:
            for item in data['items']:
                results.append({
                    'title': item.get('title', ''),
                    'url': item.get('link', ''),
                    'snippet': item.get('snippet', '')
                })
        return results
    except Exception as e:
        print(f"Search error: {e}", file=sys.stderr)
        return []


def should_search(question):
    """Ask LLM if web search is needed"""
    prompt = f"""You are a decision-making assistant. Determine if the following question requires current/recent information from the web.

Question: {question}

Respond with only "YES" if web search is needed (for current events, recent data, specific facts, etc.)
Respond with only "NO" if you can answer from general knowledge.

Response:"""

    try:
        response = model.generate_content(prompt)
        decision = response.text.strip().upper()
        return "YES" in decision
    except Exception as e:
        print(f"Decision error: {e}", file=sys.stderr)
        return False


def generate_answer(question, search_results=None):
    """Generate answer using LLM, optionally with search results"""
    if search_results:
        # Format search results for context
        context = "\n\n".join([
            f"Source: {r['title']}\nURL: {r['url']}\nContent: {r['snippet']}"
            for r in search_results
        ])

        prompt = f"""You are a helpful AI assistant. Answer the following question using the provided web search results.

Question: {question}

Web Search Results:
{context}

Provide a concise, accurate answer based on the search results. Include relevant URLs when appropriate."""
    else:
        prompt = f"""You are a helpful AI assistant. Answer the following question clearly and concisely.

Question: {question}

Answer:"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating answer: {e}"


def agent(question):
    """Main agent: decides if search is needed, searches if necessary, generates answer"""
    print(f"\n🤖 Processing: {question}\n")

    # Step 1: Decide if web search is needed
    needs_search = should_search(question)

    if needs_search:
        print("🔍 Web search needed. Searching...\n")

        # Step 2: Perform web search
        results = web_search(question)

        if results:
            print(f"✓ Found {len(results)} results\n")

            # Step 3: Generate answer with search results
            answer = generate_answer(question, results)
        else:
            print("⚠ No results found. Answering without search.\n")
            answer = generate_answer(question)
    else:
        print("💡 Answering from general knowledge\n")

        # Step 3: Generate answer without search
        answer = generate_answer(question)

    return answer


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent.py 'your question'")
        print("\nExamples:")
        print("  python agent.py 'What is the capital of France?'")
        print("  python agent.py 'What are the latest AI news?'")
        sys.exit(1)

    question = sys.argv[1]
    answer = agent(question)

    print("="*80)
    print("ANSWER:")
    print("="*80)
    print(answer)
    print("="*80)
