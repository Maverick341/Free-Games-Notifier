from typing import Final
from telegram import Update # type: ignore
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler # type: ignore
from src.config import TELEGRAM_BOT_TOKEN
from src.db.mongodb import add_subscriber, remove_subscriber

BOT_USERNAME: Final = '@FGN194_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    add_subscriber(chat_id)
    
    if update.message:
        await update.message.reply_text("✅ You're now subscribed!")

async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    remove_subscriber(chat_id)

    if update.message:
        await update.message.reply_text("❌ You've been unsubscribed.")




async def handle_user_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        message_type: str = update.message.chat.type

        print(f'User ({update.message.chat.id}) in {message_type}: "{update.message.text}')
        if message_type == 'group':
            if BOT_USERNAME in update.message.text:
                await update.message.reply_text("👋 Hello! Use /start to subscribe or /stop to unsubscribe.")
            else:
                return
        else:
            await update.message.reply_text("👋 Hello! Use /start to subscribe or /stop to unsubscribe.")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting telegram bot...')
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('stop', stop_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_user_messages))

    # Error
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)