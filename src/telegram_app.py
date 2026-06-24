from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config.settings import TOKEN
from handlers.commands import start_command, help_command, custom_command
from handlers.messages import handle_message
from handlers.admin import logs_command, stats_command

import traceback

async def error(update, context):
    print(f"Update{update} caused error {context.error}")
    traceback.print_exception(
        type(context.error),
        context.error,
        context.error.__traceback__
    )

def build_application():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(CommandHandler("logs", logs_command))
    app.add_handler(CommandHandler("stats", stats_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    return app