import os
from os import getenv

# -------------------- Telegram API Credentials --------------------

API_ID = int(getenv("API_ID", "27775431"))
API_HASH = getenv("API_HASH", "b70bb1d45a1d05236671d4cc615e40f9")

# -------------------- Bot Token & Info ----------------------------

BOT_TOKEN = getenv("BOT_TOKEN", "7930216260:AAHKqkMROgWrPeskWfYYSanLPV5x2DAkN5I")
BOT_USERNAME = getenv("BOT_USERNAME", "@Pentin_extractorbot")

# -------------------- Owner & Admins ------------------------------

OWNER_ID = int(getenv("OWNER_ID", "2446676469"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2446676469").split()))

# -------------------- Database & Logging --------------------------

MONGO_URL = getenv(
    "MONGO_URL",
    "mongodb+srv://Rohitmeena64:Ajmeer234590577@cluster0.mae8oyn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

CHANNEL_ID = int(getenv("CHANNEL_ID", "-2446676469"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-2446676469"))