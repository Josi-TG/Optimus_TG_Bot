from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get('PORT', 10000))
    print(f"Starting Flask on port {port}")
    app.run(host='0.0.0.0', port=port)


def keep_alive():
    t = Thread(target=run, deamon=True)
    t.start()