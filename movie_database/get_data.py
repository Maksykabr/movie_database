import requests


def get_data():
    count = True
    page = 1
    imdb_ids = []
    movies = []
    while True:
        # page = 1
        # api_key_1 = '9028199b'
        api_key = 'fe21051e'
        objectsListUrl = f'http://www.omdbapi.com/?apikey={api_key}&plot=full&s=movie&type=movie&r=json&page={page}&v=1'
        first_response = requests.get(objectsListUrl)
        # page = +1

        if first_response.status_code == 200:
            data = first_response.json()
            if int(data.get('totalResults', 0)) > page * 10:
                # print(f"Data for page {page}: {data}")
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
                    else:
                        print(f"Failed to retrieve data. Status code: {second_response.status_code}")
                        print("Error message:", second_response.text)
                        break
                break
                # print(imdb_ids)
        else:
            print(f"Failed to retrieve data. Status code: {first_response.status_code}")
            print("Error message:", first_response.text)
            break
    return movies

# get_data()

movies_list = get_data()

# Check if there are movies or not
if not movies_list:
    print("No movies found.")
else:
    # Print the movies
    for movie in movies_list:
        print(movie)
