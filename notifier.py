from fetch_games import get_free_games
from send_discord import send_discord_message
from send_whatsapp import send_whatsapp_message

def main():
    print("🚀 Fetching free Epic Games...")
    games = get_free_games()

    if games:
        print("✅ Free games found! Sending notifications...")
        send_discord_message(games)
        send_whatsapp_message(games)
    else:
        print("⚠️ No free games available this week.")

if __name__ == "__main__":
    main()
