import requests
from src.config import DISCORD_WEBHOOK_URL

def send_discord_message(games):
    if not DISCORD_WEBHOOK_URL:
        print("❌ Discord Webhook URL is not set.")
        return
    
    if not games:
        print("⚠️ No free games available this week.")
        return

    message = "**🔥 Epic Games Free Games This Week! 🎮**\n\n"
    for game in games:
        message += f'🆓 **{game["title"]}**\n🔗 [Claim Now](<{game["url"]}>)\n⏳ *Offer Ends: {game["end_date"]}*\n\n'

    payload = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

    if response.status_code == 204:
        print("✅ Successfully sent to Discord!")
    else:
        print(f"❌ Failed to send message. Status Code: {response.status_code}")

# Testing
if __name__ == "__main__":
    test_games = [
        {"title": "The Witcher 3", "url": "https://store.epicgames.com/en-US/p/the-witcher-3", "end_date": "Sunday, March 17, 2025 at 11:59 PM UTC"},
        {"title": "Cyberpunk 2077", "url": "https://store.epicgames.com/en-US/p/cyberpunk-2077", "end_date": "Thursday, March 20, 2025 at 10:00 AM UTC"}
    ]
    send_discord_message(test_games)
