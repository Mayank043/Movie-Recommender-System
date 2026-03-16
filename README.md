# Movie Recommendation System

This project is a Content-Based Movie Recommendation System built using Python and Machine Learning techniques.

The system recommends movies similar to the one entered by the user based on movie metadata like cast, genres, keywords, and director.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- CountVectorizer
- Cosine Similarity

## How It Works

1. Load the movie dataset
2. Select important features (keywords, cast, genres, director)
3. Combine these features into a single text column
4. Convert text into vectors using CountVectorizer
5. Calculate similarity using Cosine Similarity
6. Recommend the most similar movies

## Example

Input

```
Enter the movie: Avatar
```

Output

```
You also might like these movies...
Guardians of the Galaxy
Star Trek
John Carter
The Avengers
Alien
```

## Author

Mayank Rana
