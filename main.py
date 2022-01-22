from flask import Flask, render_template
import tmdb_client
import main as main

app = Flask(__name__)
type_list = ["popular", "now_playing", "top_rated", "upcoming"]

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=8)
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def homepage():
     movies = tmdb_client.get_popular_movies()["results"][:8]
     return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
