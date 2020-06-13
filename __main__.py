from dotenv import load_dotenv
import os
import base64
import requests
import time


load_dotenv()

secret = os.getenv("secret")


def authenticate(client_id):
    endpoint = "https://accounts.spotify.com/api/token"

    # All the weird stuff Spotify is asking us to do
    id_secret = client_id + ":" + secret
    encoded = id_secret.encode("utf-8")
    converted = base64.b64encode(encoded)
    decoded = converted.decode("utf-8")

    data = {
        "grant_type": "client_credentials"
    }
    headers = {
        "Authorization": "Basic " + decoded
    }
    r = requests.post(endpoint, data=data, headers=headers)
    json = r.json()

    current_time = time.time()
    valid_until = current_time + json["expires_in"]

    return json["access_token"], valid_until


authenticate("643f62e46f4f46b9aeb17d4d63929497")
