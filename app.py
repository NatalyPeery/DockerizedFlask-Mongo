import base64
from flask import Flask, request, render_template, make_response
from connect_to_TMDB import find_poster

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find_movie', methods=['POST'])
def find_movie():
    title = request.form['movie_title']
    movie = find_poster(title)
    if type(movie) == dict: #If we found the movie in mongo we get a dict as a return value
        response = make_response('<h1>Movie {} found in Mongo</h1><img src="data:image/jpeg;base64,{}">'.format(movie['movie_title'],base64.b64encode(movie['poster']).decode()))
    elif "https" in movie[1]:#if we found the movie in TMDB we get a list [movie_title, poster_url]
        movie_title, poster_url = movie
        response = make_response('<h1>Movie {} found in TMDB</h1><img src="{}">'.format(movie_title, poster_url))
    else:#if movie isn't found - just show the error message that we resive from find_poster function (if not movies_list:)
        response = make_response('<h1>{}</h1>'.format(movie))
    response.headers['Content-Type'] = 'text/html'
    return response


if __name__ == '__main__':
    app.run()
