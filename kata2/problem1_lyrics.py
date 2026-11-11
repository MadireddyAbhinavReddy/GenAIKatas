import numpy as np
import pandas as pd
import string

df = pd.read_csv('Lyrics Sample Dataset - Create one for me.csv')

lyrics = df['Lyrics'].values

processed_lyrics = []
for lyric in lyrics:
    lyric_lower = lyric.lower()
    lyric_clean = lyric_lower.translate(str.maketrans('', '', string.punctuation))
    processed_lyrics.append(lyric_clean)

processed_lyrics = np.array(processed_lyrics)

random_sample = np.random.choice(processed_lyrics, size=10, replace=False)

print("Random Sample of 10 Song Lyrics:\n")
for i, lyric in enumerate(random_sample, 1):
    print(f"{i}. {lyric}")
