## The Zero-Defect Pipeline: Movie Analytics
movies = [
    {"title": "Inception", "rating": 8.8, "genre": "Sci-Fi", "released": True},
    {"title": "The Room", "rating": 3.7, "genre": "Drama", "released": True},
    {"title": "Interstellar", "rating": 8.6, "genre": "Sci-Fi", "released": True},
    {"title": "Unfinished Film", "rating": 9.0, "genre": "Indie", "released": False},
    {"title": "The Godfather", "rating": 9.2, "genre": "Crime", "released": True}
]

released_movies = list(filter(lambda x: x['released'], movies))
print(released_movies)
print( )

released_movies.sort(key=lambda x: x['rating'], reverse=True)
print(released_movies)
print( )

rating_list = list(map(lambda x: x['rating'], released_movies))
print(rating_list)
print( )

from functools import reduce

total_score = reduce(lambda x,y: x+y, rating_list)
print(total_score)
print( )


def make_labeler(min_rating):
    return lambda score: "Masterpiece" if score >= min_rating else "Average"

critic_tool =  make_labeler(9.0)
print(critic_tool(total_score))