import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
import re
import os


os.environ["ANONYMIZED_TELEMETRY"] = "False"

class MovieRecommender:
    def __init__(self, csv_path="Movies Dataset - Sheet1.csv"):
        self.client = chromadb.Client()
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        try:
            self.client.delete_collection(name="movies")
        except:
            pass
        
        self.collection = self.client.create_collection(
            name="movies",
            embedding_function=self.embedding_function
        )
        
        self.load_movies(csv_path)
    
    def load_movies(self, csv_path):
        df = pd.read_csv(csv_path)
        
        ids = []
        documents = []
        metadatas = []
        
        for idx, row in df.iterrows():
            ids.append(str(idx))
            documents.append(row['Description'])
            metadatas.append({
                'title': row['Title'],
                'genre': row['Genre'],
                'director': row['Director']
            })
        
        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        
        print(f"Loaded {len(ids)} movies into ChromaDB")
    
    def build_filter(self, genre=None, director=None):
        filter_conditions = []
        
        if genre:
            filter_conditions.append({"genre": {"$eq": genre.title()}})
        
        if director:
            filter_conditions.append({"director": {"$eq": director.title()}})
        
        if len(filter_conditions) == 0:
            return None
        elif len(filter_conditions) == 1:
            return filter_conditions[0]
        else:
            return {"$and": filter_conditions}
    
    def recommend(self, query, genre=None, director=None, n_results=5):
        where_filter = self.build_filter(genre, director)
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_filter
        )
        
        recommendations = []
        
        for i in range(len(results['ids'][0])):
            recommendations.append({
                'title': results['metadatas'][0][i]['title'],
                'genre': results['metadatas'][0][i]['genre'],
                'director': results['metadatas'][0][i]['director'],
                'description': results['documents'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else None
            })
        
        return recommendations
    
    def print_recommendations(self, recommendations):
        print(f"\nTop {len(recommendations)} Recommendations:\n")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['title']}")
            print(f"   Genre: {rec['genre']}")
            print(f"   Director: {rec['director']}")
            print(f"   Description: {rec['description'][:150]}...")
            print()

def main():
    recommender = MovieRecommender()
    
    while True:
        print("\n Movie Recommendation System ")
        print("1. Search movies by description")
        print("2. Search with genre filter")
        print("3. Search with director filter")
        print("4. Search with genre and director filters")
        print("5. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            query = input("Describe what you want to watch: ")
            results = recommender.recommend(query)
            recommender.print_recommendations(results)
        
        elif choice == "2":
            query = input("Describe what you want to watch: ")
            genre = input("Genre: ")
            results = recommender.recommend(query, genre=genre)
            recommender.print_recommendations(results)
        
        elif choice == "3":
            query = input("Describe what you want to watch: ")
            director = input("Director: ")
            results = recommender.recommend(query, director=director)
            recommender.print_recommendations(results)
        
        elif choice == "4":
            query = input("Describe what you want to watch: ")
            genre = input("Genre: ")
            director = input("Director: ")
            results = recommender.recommend(query, genre=genre, director=director)
            recommender.print_recommendations(results)
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
