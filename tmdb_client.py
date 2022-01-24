

from flask import app
import requests
import tmdb_client
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYTk1ZWUxNzYxODRkYzNmODY1MGE3Njg2YjkyZTYzMCIsInN1YiI6IjYxZTk5MjM5ZGYyOTQ1MDA4ZWZhNTRjNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.u6GdwiYemVXOZjGJhmRD7_rLRou9JXJD5Fo-CH1VvtM"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = API_TOKEN
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_popular_movies()['results']
    return random.sample(data, k=len(data))[:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:how_many]

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_genres():
    endpoint = "https://api.themoviedb.org/3/genre/tv/list"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response = response.json()['genres'] 
    return response

def get_genre_movies(collection_id):
    endpoint = f"https://api.themoviedb.org/3/collection/{collection_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_by_genre(how_many, genre):
    data = get_genre_movies(genre)['results']
    return random.sample(data, k=len(data))[:how_many]

def get_movies_by_genre(how_many, genre):
    data = get_genre_movies(genre)['results']
    return random.sample(data, k=len(data))[:how_many]