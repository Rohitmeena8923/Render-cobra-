from flask import Flask
import os
import asyncio
from Extractor import info_bot  # info_bot starts your bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running on Render!"

# Start Telegram bot in the background
async def start_bot():
    await info_bot()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
