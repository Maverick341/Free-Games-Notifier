import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI, Request # type: ignore
from telegram import Update # type: ignore
from telegram.ext import Application, CommandHandler, ContextTypes # type: ignore
from telegram.ext import MessageHandler, filters # type: ignore
import uvicorn # type: ignore

from src.config import TELEGRAM_BOT_TOKEN, WEBHOOK_SECRET
from src.bot.handlers import start_command, stop_command, handle_user_messages, error

app = FastAPI()
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Add your handlers
application.add_handler(CommandHandler('start', start_command))
application.add_handler(CommandHandler('stop', stop_command))
application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_user_messages))
application.add_error_handler(error)

@app.post(f"/{WEBHOOK_SECRET}")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"status": "ok"}

if __name__=="__main__":
    uvicorn.run(app, host='0.0.0.0',port=8080)