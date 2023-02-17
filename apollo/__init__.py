# Thanks to kekikUserBot - Keyiflerolsun

from pyrogram import Client, idle
from pyrogram import __version__ as PYRO_VER
from dotenv import load_dotenv
from apollo.lib.eklentiler import userbot_eklentileri, bot_eklentileri
from pyrogram.errors import FloodWait
import logging
import os, sys

logging.getLogger("pyrogram.syncer").setLevel(
    logging.ERROR
)  # turn off pyrogram logging
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.basicConfig(level=logging.INFO)

PYTHON_VER = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
VERSION = "beta"
REPO_URL = "https://github.com/ApolloDevsTR/ApolloUserBot"

load_dotenv()

API_ID          = str(os.environ.get("API_ID", str))
API_HASH        = str(os.environ.get("API_HASH", str))
STRING_SESSION  = os.environ.get("STRING_SESSION", str)
BOT_TOKEN       = os.environ.get("BOT_TOKEN", str)
PREFIX          = os.environ.get("PREFIX", ".")
DOWNLOADS_DIR   = os.environ.get("DOWNLOADS_DIR", "downloads/")
NO_ASISTAN = False

if not os.path.isdir(DOWNLOADS_DIR): os.makedirs(DOWNLOADS_DIR)

if STRING_SESSION.startswith('-') or len(STRING_SESSION) < 351:
    logging.error("String session hatalı..!")
    quit(1)

logging.info('Apollo Userbot Başlatılıyor ...')

try:
    UserBot = Client(
        name            = "ApolloUserBot",
        api_id          = API_ID,
        api_hash        = API_HASH,
        session_string  = STRING_SESSION,
        in_memory       = True,
        plugins         = dict(root="apollo/userbot_plugins"),
    )

    Bot = Client(
        name            = "ApolloAsistan",
        api_id          = API_ID,
        api_hash        = API_HASH,
        bot_token       = BOT_TOKEN,
        in_memory       = True,
        plugins         = dict(root="apollo/bot_plugins"),
    )

except ValueError:
    logging.error("Lütfen ayarları düzgünce yapın!")
    quit(1)

CMD_HELP = {}
CMD_HELP_BOT = {}

def start():
    UserBot.start()
    try:
        Bot.start()
    except FloodWait:
        logging.warning("Asistan FloodWait yemiş, devre dışı bırakılıyor bazı özellikler çalışmayabilir!")
        NO_ASISTAN = True
    toplam_plugin_sayisi = len(userbot_eklentileri(True)) + len(bot_eklentileri(True))
    logging.info(f"ApolloUserBot 🚀 Python {PYTHON_VER} sürümünde Pyrogram {PYRO_VER} tabanında toplam {toplam_plugin_sayisi} eklentiyle çalışıyor...\n")

    idle()

    UserBot.stop()
    try:
        Bot.stop()
    except FloodWait:
        logging.error("Asistan FloodWait yemiş, devre dışı bırakılıyor bazı özellikler çalışmayabilir!")
        NO_ASISTAN = True
