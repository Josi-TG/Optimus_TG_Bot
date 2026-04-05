import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def log_message(user_id, username, chat, bot_response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    url = f"{SUPABASE_URL}/rest/v1/messages"

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "timestamp": timestamp,
        "user_id": user_id,
        "username": username,
        "chat": chat,
        "bot_response": bot_response
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code, response.text)

    print("LOGGING FUNCTION CALLED")
    print(data)


'''import sqlite3
from datetime import datetime
from config.settings import DB_PATH
from pathlib import Path

Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Messages(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TimeStamp TEXT,
    User_ID INTEGER,
    Username TEXT,
    Chat TEXT,
    bot_response TEXT

)
""")
conn.commit()


def log_message(user_id: int, username: str, chat: str, bot_response: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO Messages (TimeStamp, User_ID, Username, Chat, bot_response) VALUES (?, ?, ?, ?, ?)",
        (timestamp, user_id, username, chat, bot_response)
    )
    conn.commit()

def get_user_messages(user_id: int):
    cursor.execute(
        "SELECT TimeStamp, Chat from Messages WHERE User_ID = ? ORDER BY ID ASC",
        (user_id,)
    )
    return cursor.fetchall()

'''

