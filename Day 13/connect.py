import pprint
import requests
import pandas as pd

api_key = '345220619ebccf8d5468a83e0c69e99d'

#  EndPoint : GET /movie/{movie_id}
movie_id = 550
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'

endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
r = requests.get(endpoint)
# print(f'The text is {r.json()}')  # print out the text representation of the results (this is a string)
# pprint.pprint(r.json().keys())
"""
r.text would return a string representation of the response object whereas
r.json would return a dictionary, so we could do things like r.json.keys() etc
"""
# print(f'JSON type({type(r.json())}')
# print(endpoint)

#  EndPoint : GET /search/movie
# change the API call, this time searching for movies that contain a particular string
endpoint_path = f'/search/movie'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query=harry%20potter'
r = requests.get(endpoint)
# print(r.text)
# print(endpoint)


# Get the list of official genres for movies.
#  EndPoint : GET /genre/movie/list
# endpoint_path = f'/genre/movie/list'
# endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&language=en-US'
# r = requests.get(endpoint)
# pprint.pprint(r.json())
# print(endpoint)
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']

output = 'movies.csv'
movie_data = []

# print(results)
for _ in results:
    movie_data.append(_)
# print(movie_data)

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=True)

# # for API version 4
# import requests
#
# api_key = '345220619ebccf8d5468a83e0c69e99d'
# api_version = 4
# #  EndPoint : GET /movie/{movie_id}
# movie_id = 604
# api_bearer_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNDUyMjA2MTllYmNjZjhkNTQ2OGE4M2UwYzY5ZTk5ZCIsInN1YiI6IjYx'  \
#                    'MTE4MjE5MGI1ZmQ2MDAyYTJhZjM0YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fMaPNpegFqs' \
#                    '7TBjhxUmuVL2wBnQuZ4mBZMBF9ye5sDI '
# api_base_url = f'https://api.themoviedb.org/{api_version}'
# endpoint_path = f'/movie/{movie_id}'
# headers = {'Authorization': f'Bearer {api_bearer_token}',
#            'Content-Type': 'application/json;charset=utf-8'
#            }
#
# endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
# r = requests.get(endpoint, headers=headers)
#
# print(r.text)
