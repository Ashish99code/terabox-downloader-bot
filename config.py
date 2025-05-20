import os

def get_env_var(key, required=True):
    value = os.getenv(key)
    if required and not value:
        raise Exception(f"Missing required environment variable: {key}")
    return value

API_ID = int(get_env_var("API_ID"))
API_HASH = get_env_var("API_HASH")
BOT_TOKEN = get_env_var("BOT_TOKEN")
BOT_USERNAME = get_env_var("BOT_USERNAME")
COOKIE = get_env_var("COOKIE")

# Optional Redis settings
HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 6379))
PASSWORD = os.getenv("PASSWORD")

ADMINS = [5083063115]  # Replace with your real Telegram user ID
