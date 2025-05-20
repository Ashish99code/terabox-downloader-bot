import os

# Telegram Bot API Credentials
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "Terabox_downloader_QRbot")

# TeraBox Authentication
COOKIE = os.getenv("COOKIE")

# Telegram Chat Config
PRIVATE_CHAT_ID = int(os.getenv("PRIVATE_CHAT_ID", "-1001234567890"))
ADMINS = [int(i) for i in os.getenv("ADMINS", "").split()]

# Optional Features
FORCE_LINK = os.getenv("FORCE_LINK", "@RolodexVerse")
PUBLIC_EARN_API = os.getenv("PUBLIC_EARN_API", "")
