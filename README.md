# AI Web Explorer

A minimalistic AI agent that combines web search and LLM capabilities to intelligently answer questions with up-to-date information.

## Features

- **Intelligent Decision Making**: AI decides when web search is needed
- **Google Custom Search**: Retrieves relevant web results
- **LLM Integration**: Uses Google Gemini for answer generation
- **Three Tools in One**:
  - `agent.py` - Smart AI agent (web search + LLM)
  - `web_search.py` - Standalone web search tool
  - `web_explorer.py` - Interactive Gemini chatbot

## Setup

### 1. Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here
```

**Get API Keys:**
- Gemini API Key: https://makersuite.google.com/app/apikey
- Google Custom Search:
  1. API Key: https://developers.google.com/custom-search/v1/overview
  2. Search Engine ID: https://programmablesearchengine.google.com/

### 3. Make Scripts Executable (Optional)

```bash
chmod +x agent.py web_search.py web_explorer.py
```

## Usage

### AI Agent (Recommended)

The smart agent that decides when to search and generates comprehensive answers:

```bash
# General knowledge (no search needed)
python3 agent.py "What is the capital of France?"

# Current events (triggers web search)
python3 agent.py "What are the latest AI developments?"

# Specific recent facts (triggers web search)
python3 agent.py "Who won the 2024 Super Bowl?"
```

**Example Output:**
```
🤖 Processing: What are the latest AI developments?

🔍 Web search needed. Searching...

✓ Found 5 results

================================================================================
ANSWER:
================================================================================
Recent AI developments include... [concise summary with sources]
================================================================================
```

### Web Search Tool

Direct web search without LLM processing:

```bash
python3 web_search.py "Python tutorials"
```

### Interactive Chatbot

Chat with Gemini (no web search):

```bash
python3 web_explorer.py
```

## Project Structure

```
AI Web Explorer/
├── agent.py              # Main AI agent (web search + LLM)
├── web_search.py         # Google Custom Search tool
├── web_explorer.py       # Interactive Gemini chatbot
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your API keys (create this)
├── venv/                 # Virtual environment
└── README.md            # This file
```

## How It Works

### Agent Decision Flow

1. **Question Analysis**: LLM analyzes if the question needs current information
2. **Web Search** (if needed): Queries Google Custom Search API
3. **Answer Generation**: LLM synthesizes answer from search results or general knowledge
4. **Output**: Concise, accurate response with sources

### Example Scenarios

**Scenario 1: General Knowledge** (No search)
```
Question: "What is photosynthesis?"
→ Agent uses general knowledge
→ Fast response without web search
```

**Scenario 2: Current Events** (Triggers search)
```
Question: "What happened in the news today?"
→ Agent searches the web
→ Retrieves latest articles
→ Synthesizes summary with sources
```

## Requirements

- Python 3.8+
- Google API Key (Gemini)
- Google Custom Search Engine ID
- Internet connection

## Dependencies

All dependencies are in `requirements.txt`:
- `requests` - HTTP requests for web search
- `google-generativeai` - Gemini LLM integration
- `python-dotenv` - Environment variable management

## Troubleshooting

### Module Not Found Error
```bash
# Make sure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

### API Key Errors
- Check that `.env` file exists and contains valid keys
- Verify API keys are active in Google Cloud Console

### Search Returns No Results
- Check Search Engine ID is correct
- Verify API key has Custom Search API enabled
- Ensure you haven't exceeded daily quota (100 free searches/day)

## API Limits

- **Google Custom Search**: 100 queries/day (free tier)
- **Gemini API**: Check current limits at https://ai.google.dev/pricing

## Security

- Never commit `.env` file to version control
- Keep API keys secure and private
- Add `.env` to `.gitignore`

## License

This project is for educational purposes.

## Author

Built with Claude Code
