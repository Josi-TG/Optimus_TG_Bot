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

print("TOKEN: ", TOKEN)

print("SUPABASE_URL: ", SUPABASE_URL)

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
        print(f"BOT ALIVE - {datetime.now()}")
        time.sleep(300)  # Log every 5 minutes

def main():
    print("STEP 1 - Starting bot")

    keep_alive()
    print("STEP 2 - keep_alive returned")

    threading.Thread(target=heartbeat, daemon=True).start()

    app = Application.builder().token(TOKEN).build()
    print("STEP 3 - Application created")

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(CommandHandler("logs", logs_command))
    app.add_handler(CommandHandler("stats", stats_command))
    print("STEP 4 - Command handlers added")

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    print("STEP 5 - Message handler added")

    app.add_error_handler(error)
    print("STEP 6 - Error handler added")

    print("STEP 7 - About to start polling")

    print("Before polling")

    try:
        print("Before polling")
        app.run_polling(poll_interval=3,
                        drop_pending_updates=False
                        )
    except Exception as e:
        print("POLLING CRASHED:", e)
        raise
    finally:
        print("Polling stopped!")

    print("After polling")

    print("STEP 8 - Polling exited")



if __name__ == "__main__":
    main()