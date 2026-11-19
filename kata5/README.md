# Kata 5: Question to SQL System

## What This Does

A two-stage AI system that converts generic questions into SQL queries:

**Stage 1 - Question Refinement:**
- Takes vague questions like "show me top customers"
- Identifies the right database (sales, HR, inventory)
- Refines into specific queries with details

**Stage 2 - SQL Generation:**
- Takes the refined question
- Analyzes database schema
- Generates executable SQL query
- Explains what the query does

## How to Run

```bash
# Activate virtual environment
source ../virtualEnvironment/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running
ollama pull llama3.2
ollama serve

# Quick test
python test_kata5.py

# Full demo (processes 3 examples + interactive mode)
python question_to_sql.py
```

## Example

**Input:** "Show me the top customers"

**Stage 1 Output:**
- Refined: "Top 10 customers by total spending this year"
- Database: sales_db
- Reasoning: Customer spending data

**Stage 2 Output:**
- SQL query with proper JOINs and aggregations
- Explanation of what it does
- Tables used

## Files
- `question_to_sql.py` - Main system implementation
- `test_kata5.py` - Quick test script
- `results.json` - Demo output (auto-generated)
- `PROMPT_ANALYSIS.md` - Detailed prompt engineering analysis

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
