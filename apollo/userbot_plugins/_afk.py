from apollo.lib.CmdHelp import CmdHelp
from apollo import PREFIX, TEMP_GLOBAL
from pyrogram import Client, filters
from pyrogram.types import Message
from pathlib import Path

@Client.on_message(filters.command(['afk'], PREFIX) & filters.me)
async def afk(client:Client, message:Message):
    girilen_yazi = message.text
    length = len("afk") + len(PREFIX) + len(" ")
    sebep=girilen_yazi[+length:]

    TEMP_GLOBAL["isafk"] = True

    msg = "**Artık AFK'yım!**"
    if sebep != "":
        TEMP_GLOBAL["afkmsg"] = sebep
        await message.edit(msg + f"\n`Sebep:` {sebep}`")
    else:
        await message.edit(msg)

@Client.on_message(filters.incoming & ~filters.bot & ~filters.private)
async def on_tag(client:Client, message:Message):
    msg = "Şu an AFK'yım!"
    mentioned = message.mentioned
    rep_m = message.reply_to_message
    gme = await client.get_me()
    me = gme.id
    if mentioned or rep_m and rep_m.from_user and rep_m.from_user.id == me:
        if TEMP_GLOBAL["isafk"]:
            if TEMP_GLOBAL["afkmsg"]:
                await message.reply(msg)
            else:
                await message.reply(msg + f"\n`Sebep:` {TEMP_GLOBAL['afkmsg']}")

@Client.on_message(filters.incoming & ~filters.bot & filters.private)
async def on_pm(client:Client, message:Message):
    msg = "**Şu an AFK'yım!**"
    if TEMP_GLOBAL["isafk"]:
        if TEMP_GLOBAL["afkmsg"]:
            await message.reply(msg)
        else:
            await message.reply(msg + f"\n`Sebep:` {TEMP_GLOBAL['afkmsg']}`")

@Client.on_message(filters.command(['unafk'], PREFIX) & filters.me)
async def unafk(client:Client, message:Message):
    if TEMP_GLOBAL["isafk"]:
        await message.delete()
        await client.send_message(message.chat.id, "**Artık AFK değilim!**")
        TEMP_GLOBAL["isafk"] = False
        TEMP_GLOBAL["afkmsg"] = None
    else:
        await message.delete()

myCmdHelp = CmdHelp(Path(__file__).stem)
myCmdHelp.add_command("afk", "<İsteğe bağlı sebep>", "AFK olduğunuzu belirtir.", "afk uyuyor")
myCmdHelp.add_command("unafk", None, "AFK modunu kapatır.")
myCmdHelp.add_userbot()