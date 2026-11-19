# Kata 6: Movie Recommender System

## What This Does

A semantic movie recommendation system using ChromaDB and embeddings:

- **Loads** movie data (title, genre, director, description) from CSV
- **Creates** vector embeddings of movie descriptions
- **Stores** embeddings in ChromaDB for fast similarity search
- **Recommends** movies based on natural language queries
- Uses semantic search to find similar movies by meaning, not just keywords

## How to Run

```bash
# Activate virtual environment
source ../virtualEnvironment/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the recommender
python movie_recommender.py
```

## How It Works

1. Movie descriptions are converted to embeddings using `all-MiniLM-L6-v2`
2. Embeddings are stored in ChromaDB collection
3. When you search, your query is embedded the same way
4. ChromaDB finds the most similar movies by vector similarity
5. Returns recommendations with titles, genres, and directors

## Example Queries
- "Action movies with superheroes"
- "Romantic comedies"
- "Sci-fi space adventures"
- "Psychological thrillers"

## Files
- `movie_recommender.py` - Main recommender system
- `Movies Dataset - Sheet1.csv` - Movie database
