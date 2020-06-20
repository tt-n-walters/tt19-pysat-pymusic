import requests

from authenticate import tokens
from pprint import pprint

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

        response = r.json()[search_type + "s"]["items"]
        data = []
        for result in response:
            data.append({
                "link": result["external_urls"]["spotify"],
                "name": result["name"],
                "id": result["id"]
            })
        return data


    return search



search_artist = searcher(tokens, "artist")
search_track = searcher(tokens, "track")
    
search_track("Wish you were here")
