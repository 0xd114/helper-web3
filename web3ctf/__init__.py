from dotenv import load_dotenv
import os

load_dotenv()
INFURA_API_KEY = os.getenv('INFURA_API_KEY')

assert INFURA_API_KEY, "Get API Key freely at https://infura.io/"
