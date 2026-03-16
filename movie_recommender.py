import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv("movie_dataset.csv")
print(df.columns)

# Function to get the movie title from index
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

# Function to get the movie index from title
def get_index_from_title(title):
    try:
        return df[df.title == title]["index"].values[0]
    except:
        print(f"Movie titled '{title}' not found.")
        return None

# List of features to be used
features = ["keywords", "cast", "genres", "director"]

# Filling None values
for feature in features:
    df[feature] = df[feature].fillna("")

# Combine features into a single string
def combine_features(row):
    try:
        text = row['keywords'] + ' ' + row['cast'] + ' ' + row['genres'] + ' ' + row['director']
        return text
    except:
        print("ERROR:  ", row['index'])

df["combined_features"] = df.apply(combine_features, axis=1)

# Create a count matrix and compute cosine similarity
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

# Function to find similar movies
def movie_recommender():
    movie_user_likes = input("Enter the movie: ")
    movie_index = get_index_from_title(movie_user_likes)
    
    if movie_index is not None:
        similar_movies = list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        
        print("You also might like these movies...")
        i = 0
        for movie in sorted_similar_movies:
            print(get_title_from_index(movie[0]))
            i += 1
            if i > 5:
                break
    else:
        print("Movie not found.")

# Run the movie finder function
movie_recommender()

