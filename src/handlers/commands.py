from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I am Optimus Prime, here to help you with your questions and provide companionship. Ask me a 'Yes' or 'No' question, and I'll respond accordingly. 🤖"
    )

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text(
        "I am Optimus Prime, I come from a planet called Cybertron, here to answer questions of your intellectually challenged brain🤖"
    )

async def custom_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I still haven't decided what to put here, Stay tuned for updates! 🤖"
    )