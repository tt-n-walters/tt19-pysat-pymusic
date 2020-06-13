from dotenv import load_dotenv
import os
import base64

load_dotenv()

secret = os.getenv("secret")


def authenticate(client_id):
    endpoint = "https://accounts.spotify.com/api/token"

    # All the weird stuff Spotify is asking us to do
    id_secret = client_id + ":" + secret
    encoded = id_secret.encode("utf-8")
    converted = base64.b64encode(encoded)
    decoded = converted.decode("utf-8")

    print(decoded)

