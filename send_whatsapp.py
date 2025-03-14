from twilio.rest import Client # type: ignore
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER, USER_WHATSAPP_NUMBER

def send_whatsapp_message(games):
    if not all([TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER, USER_WHATSAPP_NUMBER]):
        print("❌ Twilio credentials are missing.")
        return

    if not games:
        print("⚠️ No free games available this week.")
        return

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message_body = "🔥 *Epic Games Free Games This Week!* 🎮\n\n"
    for game in games:
        message_body += f'🆓 *{game["title"]}*\n🔗 {game["url"]}\u200B\n⏳ Offer Ends: {game["end_date"]}\n\n'

    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=USER_WHATSAPP_NUMBER
        )
        print(f"✅ WhatsApp message sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")

# Testing
if __name__ == "__main__":
    test_games = [
        {"title": "The Witcher 3", "url": "https://store.epicgames.com/en-US/p/the-witcher-3", "end_date": "Sunday, March 17, 2025 at 11:59 PM UTC"},
        {"title": "Cyberpunk 2077", "url": "https://store.epicgames.com/en-US/p/cyberpunk-2077", "end_date": "Thursday, March 20, 2025 at 10:00 AM UTC"}
    ]
    send_whatsapp_message(test_games)
