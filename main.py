from flask import Flask, render_template
import tmdb_client
import main as main
from flask import request

app = Flask(__name__)
type_list = ["popular", "now_playing", "top_rated", "upcoming"]

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   return render_template("movie_details.html", movie=details, cast=cast)


