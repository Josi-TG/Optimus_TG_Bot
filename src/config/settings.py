import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final = os.getenv('OPTIMUS_BOT_TOKEN')
BOT_USERNAME: Final = os.getenv('OPTIMUS_USERNAME')

OWNER_ID: Final = int(os.getenv('OWNER_ID')) #Telegram user ID of the bot owner

DB_PATH: Final = os.getenv('DB_PATH') #Database file path

SUPABASE_URL: Final = os.getenv("SUPABASE_URL")
SUPABASE_KEY: Final = os.getenv("SUPABASE_KEY")