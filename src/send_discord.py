import requests
import json
from src.config import DISCORD_WEBHOOK_URLS

def send_discord_message(games):
    if not DISCORD_WEBHOOK_URLS or DISCORD_WEBHOOK_URLS == [""]:
        print("❌ Discord Webhook URLs is/are not set.")
        return
    
    if not games:
        print("⚠️ No free games available this week.")
        return
    
    message = {
    "content": "**🔥 Free Epic Games Available This Week! 🔥**\n\n"
    + "\n".join([
        f'🆓 **{game["title"]}**\n🔗 [Claim Now]({game["url"]})\n⏳ *Offer Ends: {game["end_date"]}*\n'
        for game in games
    ])
}


    headers = {"Content-Type": "application/json"}

    for webhook_url in DISCORD_WEBHOOK_URLS:
        webhook_url = webhook_url.strip()  # Remove extra spaces
        if webhook_url:
            response = requests.post(webhook_url, data=json.dumps(message), headers=headers)
            if response.status_code == 204:
                print(f"✅ Message sent successfully to {webhook_url}")
            else:
                print(f"❌ Failed to send message to {webhook_url}. Status Code: {response.status_code}")


# Testing
if __name__ == "__main__":
    test_games = [
        {"title": "The Witcher 3", "url": "https://store.epicgames.com/en-US/p/the-witcher-3", "end_date": "Sunday, March 17, 2025 at 11:59 PM UTC"},
        {"title": "Cyberpunk 2077", "url": "https://store.epicgames.com/en-US/p/cyberpunk-2077", "end_date": "Thursday, March 20, 2025 at 10:00 AM UTC"}
    ]
    send_discord_message(test_games)
