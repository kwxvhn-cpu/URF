import os
import asyncio
import threading
from dotenv import load_dotenv

load_dotenv()  # ← грузим .env ДО любых импортов проекта

from flask import Flask
from bot.main import start_bot

app = Flask(__name__)


@app.route('/')
def health():
    return 'URF is alive', 200


def run_bot():
    asyncio.run(start_bot())


if __name__ == '__main__':
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()

    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
