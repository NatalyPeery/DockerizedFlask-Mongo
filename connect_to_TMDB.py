import requests
from passwords_and_keys import api_key_to_TMDB as apk
from connect_to_mongoDB import find_poster_in_mongo

def find_poster(movie_title):
    poster_from_mongoDB = find_poster_in_mongo(movie_title)
    if not poster_from_mongoDB:
        search_movie = 'https://api.themoviedb.org/3/search/movie'
        page_num = 1
        total_movies = []
        #movie_titles = []

        while True:
            #{search_movie}?api_key={apk}=en-US&query={movie_title}&page={page_num}&include_adult=false
            params = {
                "api_key": apk,
                "query": movie_title,
                "page": page_num
            }

            response = requests.get(search_movie, params=params)
            data = response.json()
            movies_list = data.get("results")
            if not movies_list:
                return f'ERROR: Movie {movie_title} not found'
            total_movies.extend(movies_list)
            page_num += 1
            #for movie in total_movies:
                #if movie_title in movie.get("title"):
                    #title = movie.get("title")
                    #movie_titles.append(title)
            #print(total_movies[0])
            #print(movie_titles)
            movie = total_movies[0]
            movie_title = movie["title"]
            base_url = "https://image.tmdb.org/t/p/original"
            poster_url = base_url + movie['poster_path']
            return [movie_title, poster_url]
    else:
        return poster_from_mongoDB


#find_poster("scream")