import os
# Set working directory
correct_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(correct_dir)


# Load environment variables
from dotenv import load_dotenv
load_dotenv()

secret = os.getenv("secret")
client_id = os.getenv("client_id")
