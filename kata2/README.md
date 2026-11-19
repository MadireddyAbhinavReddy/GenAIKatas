# Kata 2: Text Processing with NumPy and Pandas

## What This Does

Two simple text processing programs:

**Problem 1 - Lyrics Processor:**
- Reads song lyrics from CSV
- Cleans and preprocesses text (lowercase, remove punctuation)
- Randomly samples 10 lyrics using NumPy

**Problem 2 - Review Sentiment Analysis:**
- Analyzes customer reviews from CSV
- Calculates word counts for positive vs negative reviews
- Visualizes results with histograms

## How to Run

```bash
# Activate virtual environment
source ../virtualEnvironment/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the programs
python problem1_lyrics.py
python problem2_reviews.py
```

## Files
- `problem1_lyrics.py` - Lyrics text processing
- `problem2_reviews.py` - Review sentiment analysis
- CSV files contain the datasets

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
