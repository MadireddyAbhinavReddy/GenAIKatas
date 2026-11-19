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

---

## How to Contribute / Raise a PR

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/GenAIKatas.git
   cd GenAIKatas
   ```

2. **Create a Branch**
   ```bash
   git checkout -b your-feature-name
   ```

3. **Make Changes and Commit**
   ```bash
   git add .
   git commit -m "Brief description of your changes"
   ```

4. **Push to GitHub**
   ```bash
   git push origin your-feature-name
   ```

5. **Create Pull Request**
   - Go to the repository on GitHub
   - Click "Pull requests" → "New pull request"
   - Select your branch and click "Create pull request"
   - Add a title and description
   - Submit!

**PR Guidelines:**
- Keep changes focused and small
- Test your code before submitting
- Write clear commit messages
- Describe what and why in the PR description
