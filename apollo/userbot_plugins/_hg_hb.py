from apollo.lib.CmdHelp import CmdHelp
from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep

DELAY = 0.6


@Client.on_message(filters.regex("^Hg$") & filters.me)
async def hosgeldin(client: Client, message: Message):
    hg_list = [
        "**Hoşgeldiniiiiz!**",
        "**Hg kanka 😳**",
        "**HG REİSS 😎**",
        "**Neredesin yav Hoşgeldin! **",
        "Hoşgeldin 😇",
        "**HGGGGGGG🍁**",
        "**Naber hg 🥶**",
        "**Sonunda Geldin Ha 😉**",
        "**Hoşgeldin 🔥😜**"
    ]

    for msg in hg_list:
        await message.edit(msg)
        sleep(DELAY)


@Client.on_message(filters.regex("^Hb$") & filters.me)
async def hosbuldum(client: Client, message: Message):
    hb_list = [
        "**Hoşşbulldumm 😊**",
        "**Hb hb kanka 😳**",
        "**Geldik reis 😎**",
        "**Buradayızzz hoşbulduk 😏**",
        "Hoşbuldum 😇",
        "**Hoşbulduk hoşgördük 🤠🤠🤠**",
        "**Hepinize hb🥶**",
        "**Hb 😴**",
        "**Hoşbuldum 🙂**"
    ]

    for msg in hb_list:
        await message.edit(msg)
        sleep(DELAY)

myCmdHelp = CmdHelp(Path(__file__).stem)

myCmdHelp.add_command("Hg", None,
                      "Havalı bir şekilde Hoş geldin yazar.", is_cmd=False)
myCmdHelp.add_command("Hb", None,
                      "Havalı bir şekilde Hoş buldum yazar.", is_cmd=False)
myCmdHelp.add_userbot()