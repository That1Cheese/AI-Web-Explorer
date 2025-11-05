# AI Web Explorer

AI agent that combines web search and LLM capabilities to answer questions.

## Features

- **Decision Making**: AI decides when web search is needed
- **Google Custom Search**: Retrieves relevant web results
- **LLM Integration**: Uses Google Gemini for answer generation

**Get API Keys:**
- Gemini API Key: https://makersuite.google.com/app/apikey
- Google Custom Search:
  1. API Key: https://developers.google.com/custom-search/v1/overview
  2. Search Engine ID: https://programmablesearchengine.google.com/


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
### Agent Decision Flow

1. **Question Analysis**: LLM analyzes if the question needs current information
2. **Web Search** (if needed): Queries Google Custom Search API
3. **Answer Generation**: LLM synthesizes answer from search results or general knowledge
4. **Output**: Concise, accurate response with sources

## Requirements

- Python 3.8+
- Google API Key (Gemini)
- Google Custom Search Engine ID

