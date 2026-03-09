from telegram import Update
from telegram.ext import ContextTypes
from services.response_service import handle_response
from config.settings import BOT_USERNAME

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            text = text.replace(BOT_USERNAME, "").strip()
        else:
            return
    
    response = handle_response(text)

    print("Bot: ", response)

    await update.message.reply_text(response)
