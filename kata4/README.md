# Kata 4: News Summarization Tool

## What This Does

An AI-powered news article summarizer using LangChain and Ollama:

- **Scrapes** news articles from URLs
- **Classifies** articles into categories (technology, sports, finance, etc.)
- **Generates** concise summaries using local LLM
- **Stores** summaries in JSON for later retrieval
- **Answers** questions about your saved summaries

## How to Run

```bash
# Activate virtual environment
source ../virtualEnvironment/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running with llama3.2
ollama pull llama3.2
ollama serve

# Run the CLI
python cli.py
```

## Features

1. **Summarize Articles** - Paste a URL and get an AI summary
2. **View All Summaries** - See your collection of summaries
3. **Ask Questions** - Query your summaries with natural language
4. **Auto Classification** - Articles are automatically categorized

## Files
- `summarizer.py` - Core summarization logic
- `cli.py` - Command-line interface
- `summaries.json` - Stored summaries (auto-generated)
