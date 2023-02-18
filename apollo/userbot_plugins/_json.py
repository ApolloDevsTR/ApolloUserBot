from apollo.lib.CmdHelp import CmdHelp
from apollo import PREFIX
from pyrogram import Client, filters
from pyrogram.types import Message
from pathlib import Path


@Client.on_message(filters.command(['json'], PREFIX) & filters.me)
async def jsn_ver(client: Client, message: Message):
    await message.edit(f"```{message.reply_to_message}```")

myCmdHelp = CmdHelp(Path(__file__).stem)

myCmdHelp.add_command("json", None,
                      "Bir mesajı yanıtlayın ve onun ham halini alın.")
myCmdHelp.add_userbot()
