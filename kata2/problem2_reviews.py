import pandas as pd
import string
import matplotlib.pyplot as plt

df = pd.read_csv('Customer Review - This is good. Please provide me 30 dataset rows f....csv')

def preprocess_text(text):
    text_lower = text.lower()
    text_clean = text_lower.translate(str.maketrans('', '', string.punctuation))
    return text_clean

df['processed_review'] = df['Review'].apply(preprocess_text)

df['word_count'] = df['processed_review'].apply(lambda x: len(x.split()))

positive_reviews = df[df['Sentiment'] == 'positive']
negative_reviews = df[df['Sentiment'] == 'negative']

avg_positive = positive_reviews['word_count'].mean()
avg_negative = negative_reviews['word_count'].mean()

print(f"Average word count for positive reviews: {avg_positive:.2f}")
print(f"Average word count for negative reviews: {avg_negative:.2f}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(positive_reviews['word_count'], bins=10, alpha=0.7, color='green', edgecolor='black')
plt.axvline(avg_positive, color='darkgreen', linestyle='dashed', linewidth=2)
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.title('Positive Reviews - Word Count Distribution')

plt.subplot(1, 2, 2)
plt.hist(negative_reviews['word_count'], bins=10, alpha=0.7, color='red', edgecolor='black')
plt.axvline(avg_negative, color='darkred', linestyle='dashed', linewidth=2)
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.title('Negative Reviews - Word Count Distribution')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(positive_reviews['word_count'], [1]*len(positive_reviews), 
            alpha=0.6, s=100, color='green', label='Positive')
plt.scatter(negative_reviews['word_count'], [0]*len(negative_reviews), 
            alpha=0.6, s=100, color='red', label='Negative')

sample_positive = positive_reviews.iloc[0]
plt.scatter(sample_positive['word_count'], 1, 
            s=300, color='lime', edgecolors='black', linewidths=2, 
            marker='*', label='Sample Positive Review', zorder=5)

plt.yticks([0, 1], ['Negative Cluster', 'Positive Cluster'])
plt.xlabel('Word Count')
plt.title('Sentiment Clusters based on Word Count')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f"\nSample positive review plotted: {sample_positive['Review'][:100]}...")
print(f"Word count: {sample_positive['word_count']}")
