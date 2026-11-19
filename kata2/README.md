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
