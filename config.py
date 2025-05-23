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
PRIVATE_CHAT_ID = int(os.getenv("PRIVATE_CHAT_ID", "5083063115"))  # Replace with your chat ID
FORCE_LINK = os.getenv("FORCE_LINK", "@TERABOT_DOWNLOADER")  # Replace with your channel username
PUBLIC_EARN_API = os.getenv("PUBLIC_EARN_API", "")  # Your PublicEarn API key

# Redis Configuration
HOST = os.getenv("REDIS_HOST", "localhost")
PORT = int(os.getenv("REDIS_PORT", "6379"))
PASSWORD = os.getenv("REDIS_PASSWORD", "")

ADMINS = [5083063115]  # Replace with your real Telegram user ID
