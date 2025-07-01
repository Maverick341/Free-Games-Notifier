# Free Games Notifier

A Python bot that automatically fetches the latest free titles on the Epic Games Store and notifies you via:

- 📩 Discord Webhooks  
- 💬 Telegram Bot  
- 📱 (Optional) WhatsApp via Twilio  

It can be run locally or scheduled to run weekly using GitHub Actions.

---

## 🔍 Features

- **Fetch Free Games**  
  Scrapes Epic’s free‐games API and builds a list of current zero‐price promotions.
- **Multi‐Channel Notifications**  
  - Discord: Posts rich messages via one or more Webhooks.  
  - Telegram: Sends Markdown‐formatted messages to all subscribed chat IDs (stored in MongoDB).  
  - WhatsApp (optional): Uses Twilio’s WhatsApp channel to push announcements.
- **Easy Scheduling**  
  - Local CLI: run on demand.  
  - GitHub Actions: cron schedule (every Friday at 15:00 UTC by default).

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+  
- **HTTP:** requests  
- **Env:** python-dotenv  
- **Database:** MongoDB (for Telegram subscriptions)  
- **Messaging:** Discord Webhooks, Telegram Bot API, Twilio WhatsApp  
- **CI/CD:** GitHub Actions  

---

## 🚀 Getting Started

### 1. Clone & Setup

```bash
git clone https://github.com/Maverick341/Free-Games-Notifier.git
cd Free-Games-Notifier
```

Create and activate your virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate.bat     # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 2. Configuration

Copy and edit the sample environment file:

```bash
cp .env.sample .env
```

Open `.env` and fill in **all** required values:

```.env
# Discord
DISCORD_WEBHOOK_URLS=
  https://discord.com/api/webhooks/…,
  https://discord.com/api/webhooks/…

# Twilio (WhatsApp; optional)
TWILIO_SID=
TWILIO_AUTH_TOKEN=
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
USER_WHATSAPP_NUMBER=whatsapp:+91XXXXXXXXXX

# Telegram
TELEGRAM_BOT_TOKEN=
# (Chat IDs are managed in MongoDB; see below)

# MongoDB
MONGO_URI=mongodb+srv://username:pass@cluster0.mongodb.net/mydb?retryWrites=true&w=majority
```

> ⚠️ Be sure your Bot has the right permissions and that your MongoDB user can read/write the `subscribers` collection.

---

### 3. Subscribe/Unsubscribe (Telegram)

The bot sends Telegram messages only to **subscribed** chat IDs stored in MongoDB:

- **Add** a chat ID manually:
  1. Send a message to your bot; note your chat ID from BotFather’s \`getUpdates\`.  
  2. In Mongo Shell or Compass, insert:

```js
db.subscribers.insertOne({ chat_id: 123456789, subscribed: true });
```

- **Remove** a chat ID:

```js
db.subscribers.updateOne(
  { chat_id: 123456789 },
  { $set: { subscribed: false } }
);
```

*(Future: in-bot `/subscribe` and `/unsubscribe` commands.)*

---

## 🎬 Running the Bot

### Local Execution

```bash
python -m src.notifier
```

Expected output:

```
Fetching free Epic Games...
✅ Free games found! Sending notifications...
```

---

### Scheduled (GitHub Actions)

1. Fork this repo.  
2. In **Settings → Secrets → Actions**, add the same keys from your `.env` as GitHub Secrets.  
3. Enable the `schedule.yml` workflow.  
   - By default it runs every Friday at 15:00 UTC (`0 15 * * 5`).  
   - To adjust, edit `.github/workflows/schedule.yml`.

---

## 📈 Future Improvements

- 🔄 ~~Bot commands for users to subscribe/unsubscribe via Telegram~~  
- ☁️ WhatsApp Cloud API integration  
- ✉️ Email alerts (SMTP)  
- 📊 Web dashboard for configuration & stats  

---

## 🤝 Contributing

1. Fork & branch  
2. Submit a PR with clear scope  
3. Maintain tests & doc updates  

---

## 📜 License

This project is released under the **MIT License**  
See [LICENSE](LICENSE) for details.
