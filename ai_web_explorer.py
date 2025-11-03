import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Create the model instance
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(question: str) -> str:
    """Send a question to the Gemini LLM and return the response."""
    try:
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Gemini Chatbot (type 'quit' to exit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        answer = ask_gemini(user_input)
        print(f"Gemini: {answer}\n")


