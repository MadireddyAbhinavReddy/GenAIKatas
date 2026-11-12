# Movie Recommendation System with ChromaDB

A semantic search-based movie recommendation system using ChromaDB vector database and sentence embeddings.

## Features

- Semantic search based on movie descriptions
- Filter by genre and director
- Uses sentence transformers for embeddings
- Returns top 5 most relevant movies
- Interactive CLI interface

## Installation

```bash
cd kata6
pip install -r requirements.txt
```

## Usage

### Interactive Mode

```bash
python movie_recommender.py
```

Menu options:
1. Search by description only
2. Search with genre filter
3. Search with director filter  
4. Search with both filters

### Test Examples

```bash
python test_examples.py
```

Runs 8 example queries showing different search scenarios.

## How It Works

### 1. Data Loading

Movies are loaded from CSV with:
- Title
- Description (embedded)
- Genre (metadata)
- Director (metadata)

### 2. Embedding Generation

Uses `all-MiniLM-L6-v2` sentence transformer model to convert descriptions into 384-dimensional vectors.

### 3. Vector Storage

ChromaDB stores:
- Document: Movie description
- Embedding: Vector representation
- Metadata: Genre and director

### 4. Query Processing

User query is embedded and compared against stored movie embeddings using cosine similarity.

### 5. Filtering

ChromaDB filters applied before similarity search:
- Genre filter: `{"genre": {"$eq": "Science Fiction"}}`
- Director filter: `{"director": {"$eq": "Christopher Nolan"}}`
- Combined: `{"$and": [condition1, condition2]}`

### 6. Results

Returns top 5 most similar movies based on embedding distance.

## Example Queries

**Query:** "mind-bending psychological thriller with twists"
**Results:** Memento, The Prestige, Inception, The Sixth Sense, Se7en

**Query:** "space exploration" + Genre: "Science Fiction" + Director: "Christopher Nolan"
**Results:** Interstellar, Inception

**Query:** "mafia and organized crime family" + Genre: "Crime"
**Results:** The Godfather, The Departed, Pulp Fiction

## Architecture

```
User Query
    ↓
Embedding Function (SentenceTransformer)
    ↓
Query Vector
    ↓
ChromaDB Vector Search (with filters)
    ↓
Top 5 Similar Movies
```

## Technical Details

**Embedding Model:** all-MiniLM-L6-v2
- Dimensions: 384
- Fast inference
- Good quality for semantic similarity

**Distance Metric:** Cosine similarity (default in ChromaDB)

**Filter Operators:**
- `$eq` - Exact match
- `$and` - Logical AND for multiple conditions

## Limitations

- Requires exact genre/director names (case-sensitive)
- Limited to text descriptions (no images or trailers)
- Cold start: All movies need to be pre-loaded

## Future Enhancements

- Fuzzy matching for genre/director names
- User ratings and collaborative filtering
- Hybrid recommendations (content + collaborative)
- Movie posters and trailer integration
- User preference learning
