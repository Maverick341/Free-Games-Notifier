import requests
from src.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(games):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Telegram Bot Token or Chat ID is not set.")
        return
    
    if not games:
        print("⚠️ No free games available this week.")
        return
    

    message = "**🔥 Free Epic Games Available This Week! 🔥**\n\n" + "\n".join([
        f'🆓 *{game["title"]}*\n🔗 [Claim Now]({game["url"]})\n⏳ _Offer Ends: {game["end_date"]}_\n'
        for game in games
    ])

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("✅ Telegram message sent successfully!")
    else:
        print(f"❌ Error sending message: {response.text}")

if __name__ == "__main__":
    test_games = [
        {"title": "The Witcher 3", "url": "https://store.epicgames.com/en-US/p/the-witcher-3", "end_date": "Sunday, March 17, 2025 at 11:59 PM UTC"},
        {"title": "Cyberpunk 2077", "url": "https://store.epicgames.com/en-US/p/cyberpunk-2077", "end_date": "Thursday, March 20, 2025 at 10:00 AM UTC"}
    ]
    send_telegram_message(test_games)