from apollo.lib.CmdHelp import CmdHelp
from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import sleep

DELAY = 0.6


@Client.on_message(filters.regex("^Sa$") & filters.outgoing)
async def selamunaleykum(client: Client, message: Message):
    sa_list = [

        "**🍖🔥Sea**",
        "**S ve A❄️**",
        "**SEA🔥**",
        "**Selam Almayanın😡 **",
        "🌀Sea",
        "**🧿Slm**",
        "**🇹🇷Sa🇦🇿**",
        "**Selam🍁**",
        "**❄️Naber**",
        "**Ben Geldim💬**",
        "**Hoşgeldim💋**",
        "**🚀 Selamün Aleyküm🔥**"

    ]

    for msg in sa_list:
        await message.edit(msg)
        sleep(DELAY)


@Client.on_message(filters.regex("^As$") & filters.outgoing)
async def aleykumselam(client: Client, message: Message):
    as_list = [

        "**🍖🔥Ase**",
        "**A ve S❄️**",
        "**🧿As**",
        "**Bizde Seni Bekliyorduk Hoşgeldin 💋 **",
        "🌀Ase",
        "**❄️As**",
        "**🇹🇷Ase🇦🇿**",
        "**Aleyküm Selam🍁**",
        "**❄️Nabre**",
        "**Sonunda Geldin💬**",
        "**Hoşgeldin🔥😜**",
        "**Aleyküm Selam...🚀**"

    ]

    for msg in as_list:
        await message.edit(msg)
        sleep(DELAY)

myCmdHelp = CmdHelp(Path(__file__).stem)

myCmdHelp.add_command("Sa", None,
                      "Havalı bir şekilde Selamün aleyküm yazar.", is_cmd=False).add_userbot()
myCmdHelp.add_command("As", None,
                      "Havalı bir şekilde Aleyküm Selam yazar.", is_cmd=False).add_userbot()
