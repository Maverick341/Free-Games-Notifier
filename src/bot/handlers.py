from typing import Final
from telegram import Update # type: ignore
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler # type: ignore
from src.config import TELEGRAM_BOT_TOKEN
from src.db.mongodb import add_subscriber, remove_subscriber

BOT_USERNAME: Final = '@FGN194_bot'

async def is_user_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    chat = update.effective_chat
    user = update.effective_user

    if chat.type in ['group', 'supergroup', 'channel']:
        member = await context.bot.get_chat_member(chat.id, user.id)
        return member.status in ['administrator', 'creator']
    
    return True  # In private chat, allow by default


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if not await is_user_admin(update, context):
        await update.message.reply_text("🚫 Only admins can start the bot in this chat.")
        return
    
    response = add_subscriber(chat_id)
    if update.message:
        await update.message.reply_text(response)

async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if not await is_user_admin(update, context):
        await update.message.reply_text("🚫 Only admins can stop the bot in this chat.")
        return
    
    response = remove_subscriber(chat_id)
    if update.message:
        await update.message.reply_text(response)




async def handle_user_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    
    message_type: str = update.message.chat.type
    user_message = update.message.text or ""

    print(f'User ({update.message.chat.id}) in {message_type}: "{user_message}"')

    if message_type == 'channel':
        # Skip handling channel messages
        return
    
    if message_type in ['group', 'supergroup']:
        if BOT_USERNAME in user_message:
            await update.message.reply_text("👋 Hello! Use /start to subscribe or /stop to unsubscribe.")
        else:
            return
    elif message_type == 'private':
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
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_user_messages))

    # Error
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)