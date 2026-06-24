from telegram import Update
from telegram.ext import ContextTypes
from src.services.response_service import handle_response
from src.services.logger_service import log_message
from src.config.settings import BOT_USERNAME

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text = update.message.text
    user_id = update.message.chat.id
    username = update.message.from_user.username or update.message.from_user.full_name

    #log EVERY message



    print(f'User ({user_id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            text = text.replace(BOT_USERNAME, "").strip()
        else:
            return
    
    response = handle_response(text)

    print("Bot: ", response)

    await update.message.reply_text(response)

    log_message(user_id, username, text, response)

    '''log_message(update.message.from_user.id, update.message.from_user.username or update.message.from_user.full_name, text, response)
'''