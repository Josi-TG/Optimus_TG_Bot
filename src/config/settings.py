import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final = os.getenv('OPTIMUS_BOT_TOKEN')
BOT_USERNAME: Final = os.getenv('OPTIMUS_USERNAME')