import requests

from authenticate import tokens


def searcher(tokens, search_type):
    def search(query):
        endpoint = "https://api.spotify.com/v1/search"
        headers = {
            "Authorization": "Bearer " + next(tokens)
        }
        parameters = {
            "q": query,
            "type": search_type,
            "limit": 50
        }
        r = requests.get(endpoint, params=parameters, headers=headers)
        print(r.json())
    return search



search_artist = searcher(tokens, "artist")
search_track = searcher(tokens, "track")
    
search_artist("Queen")
