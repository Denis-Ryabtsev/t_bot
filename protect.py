from dotenv import load_dotenv
import os


load_dotenv()
ALLOWED_USERS = os.getenv('USERS')

def check_user(id: int) -> bool:
    return str(id) in ALLOWED_USERS