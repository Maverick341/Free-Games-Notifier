import requests
import json
from src.config import TELEGRAM_BOT_TOKEN
from src.db.mongodb import get_subscribed_chat_ids

def send_telegram_message(games):
    if not TELEGRAM_BOT_TOKEN:
        print("❌ Telegram Bot Token or Chat ID is not set.")
        return
    
    chat_ids = get_subscribed_chat_ids()
    if not chat_ids:
        print("ℹ️ No subscribed chat IDs found.")
        return

    if not games:
        print("⚠️ No free games available this week.")
        return
    

    message = "**🔥 Free Epic Games Available This Week! 🔥**\n\n" + "\n".join([
        f'🆓 *{game["title"]}*\n🔗 [Claim Now]({game["url"]})\n⏳ _Offer Ends: {game["end_date"]}_\n'
        for game in games
    ])

    headers = {"Content-Type": "application/json"}

    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }

        response = requests.post(url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            print(f"✅ Telegram Message sent successfully to Chat ID: {chat_id}")
        else:
            print(f"❌ Error sending message to {chat_id}: {response.text}")

if __name__ == "__main__":
    test_games = [
        {"title": "The Witcher 3", "url": "https://store.epicgames.com/en-US/p/the-witcher-3", "end_date": "Sunday, March 17, 2025 at 11:59 PM UTC"},
        {"title": "Cyberpunk 2077", "url": "https://store.epicgames.com/en-US/p/cyberpunk-2077", "end_date": "Thursday, March 20, 2025 at 10:00 AM UTC"}
    ]
    send_telegram_message(test_games)