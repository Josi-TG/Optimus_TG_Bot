from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config.settings import TOKEN
from handlers.commands import start_command, help_command, custom_command
from handlers.messages import handle_message


async def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    print("Starting bot...")

    app = Application.builder().token(TOKEN).build()

    #Command Handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    #Message Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Error Handler
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()