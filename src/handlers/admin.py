from telegram import Update
from telegram.ext import ContextTypes
import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

async def logs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"{SUPABASE_URL}/rest/v1/messages?select=*&order=id.desc&limit=5"

    headers = {
        "apikey" : SUPABASE_KEY,
        "Authorization" : f"Bearer {SUPABASE_KEY}"
    }

    response = requests.get(url, headers=headers)

    logs = response.json()

    print("LOGS COMMAND TRIGGERED")

    print(logs)

    print(type(logs))

    if not logs:
        await update.message.reply_text("No logs found.")
        return
    
    text = ""

    for log in logs:
        text += (
            f"👤 {log['username']}\n"
            f"💬 {log['chat']}\n"
            f"🤖 {log['bot_response']}\n\n"
        )

    await update.message.reply_text(text)

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"{SUPABASE_URL}/rest/v1/messages?select=*"

    headers = {
        "apikey" : SUPABASE_KEY,
        "Authorization" : f"Bearer {SUPABASE_KEY}"
    }

    response = requests.get(url, headers=headers)

    logs = response.json()

    print("STATS COMMAND TRIGGERED")

    total_messages = len(logs)

    users = {}

    for log in logs:
        username = log['username']

        if username not in users:
            users[username] = 0
        
        users[username] += 1

    total_users = len(users)

    most_active = max(users, key=users.get)

    text = (
        f"Bot Stats\n\n"
        f"Total Messages: {total_messages}\n"
        f"Total Users: {total_users}\n\n"
        f"Most Active User: {most_active}"
    )

    await update.message.reply_text(text)

