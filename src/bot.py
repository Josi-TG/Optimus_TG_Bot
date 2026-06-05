import threading
import time
from datetime import datetime

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config.settings import TOKEN, SUPABASE_URL
from handlers.commands import start_command, help_command, custom_command
from handlers.messages import handle_message
from handlers.admin import logs_command, stats_command

from webserver import keep_alive

import signal

def handle_sigterm(signum, frame):
    print(f"RECEIVED SIGNAL: {signum}")

signal.signal(signal.SIGTERM, handle_sigterm)
signal.signal(signal.SIGINT, handle_sigterm)

import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


import traceback

async def error(update, context):
    print(f"Update {update} caused error {context.error}")
    traceback.print_exception(
        type(context.error),
        context.error,
        context.error.__traceback__
    )

def heartbeat():
    while True:
        print(
            f"BOT ALIVE | THREADS={threading.active_count()} | TIME={datetime.now()}"
        )
        time.sleep(300)  # Log every 5 minutes
        

def main():


    keep_alive()


    threading.Thread(target=heartbeat, daemon=True).start()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(CommandHandler("logs", logs_command))
    app.add_handler(CommandHandler("stats", stats_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)


    print("Starting polling...")

    app.run_polling(
        poll_interval=3,
        drop_pending_updates=False,
        stop_signals=None
    )




if __name__ == "__main__":
    main()