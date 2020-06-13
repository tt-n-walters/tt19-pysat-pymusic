from dotenv import load_dotenv
import os

load_dotenv()

secret = os.getenv("secret")


def authenticate(client_id):
    endpoint = "https://accounts.spotify.com/api/token"

