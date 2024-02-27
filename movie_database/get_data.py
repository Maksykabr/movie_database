import requests


def get_data():
    count = 1
    page = 1
    imdb_ids = []
    movies = []
    while True:
        api_key = '77e34546'
        objectsListUrl = f'http://www.omdbapi.com/?apikey={api_key}&plot=full&s=movie&type=movie&r=json&page={page}&v=1'
        first_response = requests.get(objectsListUrl)

        if first_response.status_code == 200:
            data = first_response.json()
            if int(data.get('totalResults', 0)) > page * 10:
                for movie in data['Search']:
                    imdb_ids.append(movie['imdbID'])
                page += 1
            else:
                print("No more pages. Exiting.")
                for movie_id in imdb_ids:
                    getMovieUrl = f'http://www.omdbapi.com/?apikey={api_key}&i={movie_id}&r=json'
                    second_response = requests.get(getMovieUrl)
                    if second_response.status_code == 200:
                        movie_data = second_response.json()
                        if 'Error' in movie_data and movie_data['Error'] == 'Incorrect IMDb ID.':
                            print(f"No data found for IMDb ID: {movie_id}")
                        else:
                            movies.append(movie_data)
                            print('movie data is ready')
                    else:
                        print(f"Failed to retrieve data. Status code: {second_response.status_code}")
                        print("Error message:", second_response.text)
                        break

                    print(f'movie data is ready{count}')
                    count += 1
                break
        else:
            print(f"Failed to retrieve data. Status code: {first_response.status_code}")
            print("Error message:", first_response.text)
            break
    return movies


movies_list = get_data()


def prepared_data(movies_list):
    prepared_movies = []

    for movie in movies_list:
        prepared_movie = {
            "title": movie.get("Title", ""),
            "release_year": movie.get("Year", ""),
            "director": movie.get("Director", ""),
            "actors": movie.get("Actors", "").split(', ') if movie.get("Actors") else [],
        }
        print(prepared_movie)
        prepared_movies.append(prepared_movie)

    return prepared_movies


prepared_movies_data = prepared_data(movies_list)
