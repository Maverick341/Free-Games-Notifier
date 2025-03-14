# Epic Games Free Games Notifier

This project automatically fetches free games from the **Epic Games Store** and sends notifications via **WhatsApp (Twilio)** and **Discord Webhooks**.

## 🚀 Features
- Fetches **weekly free games** from the Epic Games Store.
- Sends notifications via **WhatsApp (Twilio API)**.
- Notifies in **Discord channels** using webhooks.
- Can be run **locally** or via **GitHub Actions (Scheduled Run)**.

---

## 🖥️ 1️⃣ Running the Bot Locally

### **Step 1: Clone the Repository**  
```sh
git clone https://github.com/your-username/epic-games-notifier.git
cd epic-games-notifier
```

### **Step 2: Set Up Python Environment**  
Ensure you have **Python 3.8+** installed. 
Create a virtual environment (recommended):  
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Step 3: Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **Step 4: Configure Environment Variables**  
Create a `.env` file in the project folder and add the following variables:
```ini
DISCORD_WEBHOOK_URL=your_discord_webhook_url
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
USER_WHATSAPP_NUMBER=whatsapp:+your_number
```
⚠ **Note:** You must add your own **Discord Webhook URL**, **Twilio API credentials**, and **Twilio WhatsApp number**. You also need to **set up Twilio Sandbox** to send and receive messages.

### **Step 5: Run the Bot**  
```sh
python notifier.py
```
This will fetch the free games and send notifications via **WhatsApp & Discord**.

---

## 🌐 2️⃣ Running the Bot on a GitHub Fork (Using GitHub Actions)

### **Step 1: Fork the Repository**  
Go to the **original repo** → Click **Fork**.

### **Step 2: Set Up GitHub Secrets**  
1. Go to your **forked repo** on GitHub.
2. Navigate to **Settings → Secrets and variables → Actions → New repository secret**.
3. Add the following secrets (**without quotes**):
   ```sh
   DISCORD_WEBHOOK_URL=your_discord_webhook_url
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
   USER_WHATSAPP_NUMBER=whatsapp:+your_number
   ```
   ⚠ **Note:** Each user must configure their own **Discord Webhook**, **Twilio credentials**, and **Twilio WhatsApp number** in GitHub Secrets.

### **Step 3: Enable GitHub Actions**  
1. Go to your repo’s **Actions** tab.
2. Click on the **workflow file** (e.g., `.github/workflows/schedule.yml`).
3. Enable workflows if prompted.

### **Step 4: Edit the Schedule (Optional)**  
- The bot is set to run **every Friday at 8 AM PT** (Epic Games’ schedule).
- To change the schedule, edit `.github/workflows/schedule.yml`:
  ```yaml
  schedule:
    - cron: "0 15 * * 5"  # Runs every Friday at 8 AM PT (15:00 UTC)
  ```

### **Step 5: Commit & Push Changes**  
```sh
git add .
git commit -m "Updated GitHub Actions workflow"
git push origin main
```
The bot will now **run automatically every week** and send notifications.

---

## 📜 License  
This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing  
Feel free to submit pull requests to improve this project!

---
