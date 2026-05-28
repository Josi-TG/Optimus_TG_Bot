from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config.settings import TOKEN, SUPABASE_URL
from handlers.commands import start_command, help_command, custom_command
from handlers.messages import handle_message
from handlers.admin import logs_command, stats_command

from webserver import keep_alive

print("TOKEN: ", TOKEN)

print("SUPABASE_URL: ", SUPABASE_URL)

async def error(update, context):
    print(f"Update {update} caused error {context.error}")



def main():
    print("Starting bot...")


    keep_alive()

    app = Application.builder().token(TOKEN).build()

    #Command Handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(CommandHandler("logs", logs_command))
    app.add_handler(CommandHandler("stats", stats_command))

    #Message Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Error Handler
    app.add_error_handler(error)


    print("Polling...")
    print("Bot connected to Telegram successfully")
    app.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()