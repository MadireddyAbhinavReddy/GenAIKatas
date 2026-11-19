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
