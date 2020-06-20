import base64
import time

import requests

from config import client_id, secret


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


def token_generator(client_id):
    token = None
    valid_until = 0

    while True:
        # Check if expired
        if time.time() > valid_until:
            token, valid_until = authenticate(client_id)
        yield token


tokens = token_generator()
