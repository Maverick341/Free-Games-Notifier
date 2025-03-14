import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration variables
DISCORD_WEBHOOK_URLS = os.getenv("DISCORD_WEBHOOK_URLS", "").split(',')
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
USER_WHATSAPP_NUMBER = os.getenv("USER_WHATSAPP_NUMBER")
EPIC_FREE_GAMES_URL = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US"
