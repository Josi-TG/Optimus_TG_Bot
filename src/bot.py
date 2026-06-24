from datetime import datetime

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from src.config.settings import TOKEN, SUPABASE_URL
from src.handlers.commands import start_command, help_command, custom_command
from src.handlers.messages import handle_message
from src.handlers.admin import logs_command, stats_command


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


def main():

    print(f"BOT STARTED AT {datetime.now()}")


    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(CommandHandler("logs", logs_command))
    app.add_handler(CommandHandler("stats", stats_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)


    try:
        print("Before polling")
        app.run_polling(poll_interval=3,
                        drop_pending_updates=False,
                        stop_signals=None
                        )
    except Exception as e:
        print("POLLING CRASHED:", e)
        raise
    finally:
        print("Polling stopped!")

    print("After polling")




if __name__ == "__main__":
    main()