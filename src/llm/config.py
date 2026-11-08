import os
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("MODEL")
BASE_URL = os.getenv("BASE_URL")

if not MODEL or not BASE_URL:
    raise ValueError("Не заданы переменные окружения MODEL или BASE_URL")