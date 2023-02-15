from pyrogram.types import Message
from pyrogram import Client, filters
from apollo import VERSION, PYTHON_VER, PYRO_VER
from apollo.lib.eklentiler import userbot_eklentileri, bot_eklentileri
from apollo.CmdHelp import CmdHelp
from apollo import PREFIX
from pathlib import Path
from os import listdir

@Client.on_message(filters.command("alive", PREFIX) & filters.me)
async def alive(client: Client, message: Message):
    if message.forward_from:
        return
    
    chat = message.chat.id
    
    await message.edit("__Yükleniyor...__")

    toplam_plugin_sayisi = len(userbot_eklentileri(True)) + len(bot_eklentileri(True))

    await message.delete()
    text = f"**ApolloUserBot Çalışıyor 🚀**\n__Python versiyonu:__ `{PYTHON_VER}`\n__Pyrogram versiyonu:__ `{PYRO_VER}`\n__Bot versiyonu:__ `{VERSION}`\n__Eklenti sayınız:__ `{toplam_plugin_sayisi}`"
    await client.send_photo(chat, "https://telegra.ph/file/395921861f2acd8869119.png", text)

CmdHelp(Path(__file__).stem).add_command("alive", None, "Bot yaşıyor mu ona bakar.").add_userbot()