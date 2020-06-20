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
            item = {
                "link": result["external_urls"]["spotify"],
                "name": result["name"],
                "id": result["id"]
            }
            if search_type == "track":
                item["artist_name"] = result["artists"][0]["name"]

            data.append(item)

        return data

    return search


search_artist = searcher(tokens, "artist")
search_track = searcher(tokens, "track")


def get_recommendations(token, artists=[], tracks=[]):
    artist_string = ",".join(artists)
    track_string = ",".join(tracks)

    parameters = {}
    if artist_string:
        parameters["seed_artists"] = artist_string
    if track_string:
        parameters["seed_tracks"] = track_string
    
    endpoint = "https://api.spotify.com/v1/recommendations"
    headers = {
        "Authorization": "Bearer " + token
    }
    r = requests.get(endpoint, params=parameters, headers=headers)

    response = r.json()[search_type + "s"]["items"]
    data = []
    for result in response:
        item = {
            "link": result["external_urls"]["spotify"],
            "name": result["name"],
            "id": result["id"]
        }
        if search_type == "track":
            item["artist_name"] = result["artists"][0]["name"]

        data.append(item)

    return data


    
# search_track("Wish you were here")

get_recommendations(next(tokens), artists=["0k17h0D3J5VfsdmQ1iZtE9"])
