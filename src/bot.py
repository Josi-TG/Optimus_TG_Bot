from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from magic8ball import yesOrNo
from magic8ball import quotes

TOKEN: Final = '8683549610:AAE-iufmHTT0VXPNES6qRzVKf6W_oqdA7xA'
BOT_USERNAME: Final = '@PythonOptimusBot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am Optimus Prime, here to help you with your questions and provide companionship. Ask me a 'Yes' or 'No' question, and I'll respond accordingly. 🤖")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am Optimus Prime, I come from a planet called Cybertron, here to answer questions of your intellectually challenged brain🤖")



async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I still haven't decided what to put here, Stay tuned for updates! 🤖")

#Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello there! '
    if 'how are you' in processed:
        return 'I am doing well, thank you for asking 👈(ﾟヮﾟ👈)'
    if 'what is your name' in processed or "what's your name" in processed or "who are you" in processed:
        return "I am Optimus Prime, AKA leader of the AutoBots, AKA Decepticon Demolisher, AKA Fulltime Energon sniffing expert, either you stand beside me or choke on my blaster while you grind and gurgle my sword with your teeth through the back of your skull. ♨︎_♨︎"
    if 'say something cool' in processed or 'say something deep' in processed:
        return quotes()
    
    return yesOrNo()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print(f'Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #Polling
    print('Polling...')
    app.run_polling(poll_interval=3)
