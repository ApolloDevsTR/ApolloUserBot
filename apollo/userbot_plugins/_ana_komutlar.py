from apollo import CMD_HELP, CMD_HELP_BOT, STRING_SESSION, BOT_TOKEN, API_ID, API_HASH, REPO_URL, PREFIX, PYTHON_VER, PYRO_VER, VERSION
from apollo.lib.eklentiler import userbot_eklentileri, bot_eklentileri
from apollo.lib.helpers import kullanici, yanitlanan_mesaj, pyro_hata
from apollo.lib.CmdHelp import CmdHelp
from pyrogram import Client, filters
from pathlib import Path
from pyrogram.types import Message
from time import time
import asyncio
import os

@Client.on_message(filters.command(['help', 'yardim'], PREFIX) & filters.me)
async def send_info(client:Client, message:Message):
    basla = time()
    await message.edit("__Yükleniyor__...")

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id}).\n
Ben 𝘼𝙥𝙤𝙡𝙡𝙤 𝙐𝙨𝙚𝙧𝘽𝙤𝙩 🚀 ve sizin hizmetinizdeyim!\n
Kaynak kodlarım [burada]({REPO_URL}).
Kullanabileceğin komutlar ise eklentilerimde gizli..\n\n"""

    mesaj += """__Userbot eklentilerini görebilmek için__ `.ulist`, Asistan eklentilerini görebilmek için__ `.blist` __komutunu kullanabilirsin..__
`.uapollo` veya `.bapollo` «__eklenti__» **komutuyla da userbot veya asistan eklentisi hakkında bilgi alabilirsin..**
__Not: Sadece `.apollo` v.s. yazarak hedef belirtmezseniz varsayılan olarak userbot için işlem yaparsınız.
""" #TODO: buraya kanalların linklerini de koy

    bitir = time()
    sure = bitir - basla
    mesaj += f"\n**Ping :** `{sure * 1000:.3f} ms`"


    await message.edit(mesaj, disable_web_page_preview=True)

@Client.on_message(filters.command(['apollo', 'uapollo'], PREFIX) & filters.me)
async def bot_help(client:Client, message:Message):

    ilk_mesaj = await message.edit('`Hallediyorum..`', disable_web_page_preview = True)

    if len(message.command[1]) == 1:
        mesaj = "`EklentiAdı` **Girmelisin!**\n\n"

        await ilk_mesaj.edit(mesaj)
        return

    try:
        mesaj = CMD_HELP[message.command[1]]
    except KeyError:
        mesaj = f"`{message.command[1]}`\n\t**adında bir eklenti bulunamadı..**"

    await ilk_mesaj.edit(mesaj)

@Client.on_message(filters.command(['bapollo'], PREFIX) & filters.me)
async def userbot_help(client:Client, message:Message):

    ilk_mesaj = await message.edit('`Hallediyorum..`', disable_web_page_preview = True)

    if len(message.command[1]) == 1:
        mesaj = "`EklentiAdı` **Girmelisin!**\n\n"

        await ilk_mesaj.edit(mesaj)
        return

    try:
        mesaj = CMD_HELP_BOT[message.command[1]]
    except KeyError:
        mesaj = f"`{message.command[1]}`\n\t**adında bir eklenti bulunamadı..**"

    await ilk_mesaj.edit(mesaj)

@Client.on_message(filters.command(['plist', 'ulist'], PREFIX) & filters.me)
async def userbot_eklenti_list(client:Client, message:Message):

    ilk_mesaj = await message.edit("__Yükleniyor__...", disable_web_page_preview = True)

    mesaj = "__*-Userbot Eklentileri-*__\n"
    mesaj += userbot_eklentileri()

    await ilk_mesaj.edit(mesaj)

@Client.on_message(filters.command(['blist'], PREFIX) & filters.me)
async def bot_eklenti_list(client:Client, message:Message):

    ilk_mesaj = await message.edit("__Yükleniyor__...", disable_web_page_preview = True)

    mesaj = "__*-Asistan Eklentileri-*__\n"
    mesaj += bot_eklentileri()

    await ilk_mesaj.edit(mesaj)

@Client.on_message(filters.command(['pget', 'uget'], PREFIX) & filters.me)
async def userbot_eklenti_ver(client:Client, message:Message):

    ilk_mesaj = await message.edit("__Yükleniyor...__", disable_web_page_preview = True)
    yanit_id  = await yanitlanan_mesaj(message)

    if len(message.command) == 1:
        await ilk_mesaj.edit("`EklentiAdı` **Girmelisin!**")
        return

    dosya = message.command[1]

    if f"{dosya}.py" in os.listdir("apollo/userbot_plugins"):
        await ilk_mesaj.delete()

        await message.reply_document(
            document                = f"./apollo/userbot_plugins/{dosya}.py",
            caption                 = f"__ApolloUserBot 🚀__ `{dosya}` __eklentisi..__",
            disable_notification    = True,
            reply_to_message_id     = yanit_id
            )

    else:
        await ilk_mesaj.edit('**Eklenti Bulunamadı!**')

@Client.on_message(filters.command(['bget'], PREFIX) & filters.me)
async def bot_eklenti_ver(client:Client, message:Message):

    ilk_mesaj = await message.edit("__Yükleniyor...__", disable_web_page_preview = True)
    yanit_id  = await yanitlanan_mesaj(message)

    if len(message.command) == 1:
        await ilk_mesaj.edit("`EklentiAdı` **Girmelisin!**")
        return

    dosya = message.command[1]

    if f"{dosya}.py" in os.listdir("apollo/bot_plugins"):
        await ilk_mesaj.delete()

        await message.reply_document(
            document                = f"./apollo/bot_plugins/{dosya}.py",
            caption                 = f"__ApolloAsistan 🚀__ `{dosya}` __eklentisi..__",
            disable_notification    = True,
            reply_to_message_id     = yanit_id
            )

    else:
        await ilk_mesaj.edit('**Eklenti Bulunamadı!**')

@Client.on_message(filters.command(['pinstall', 'uinstall'], PREFIX) & filters.me)
async def userbot_eklenti_al(client:Client, message:Message):

    ilk_mesaj = await message.edit("__Yükleniyor...__", disable_web_page_preview = True)
    cevaplanan_mesaj = message.reply_to_message

    if len(message.command) == 1 and cevaplanan_mesaj.document:
        if cevaplanan_mesaj.document.file_name.split(".")[-1] != "py":
            await ilk_mesaj.edit("`Yalnızca python dosyası yükleyebilirsiniz..`")
            return
        eklenti_dizini = f"./apollo/userbot_plugins/{cevaplanan_mesaj.document.file_name}"
        await ilk_mesaj.edit("`Eklenti Yükleniyor...`")

        if os.path.exists(eklenti_dizini):
            await ilk_mesaj.edit(f"`{cevaplanan_mesaj.document.file_name}` __eklentisi zaten mevcut!__")
            return

        try:
            await client.download_media(message=cevaplanan_mesaj, file_name=eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Eklenti Yüklendi:** `{cevaplanan_mesaj.document.file_name}`")
            return

        except Exception as hata:
            await pyro_hata(hata, ilk_mesaj)
            return

    await ilk_mesaj.edit('__Python betiği yanıtlamanız gerekmektedir__')

@Client.on_message(filters.command(['binstall'], PREFIX) & filters.me)
async def bot_eklenti_al(client:Client, message:Message):

    ilk_mesaj = await message.edit("__Yükleniyor...__", disable_web_page_preview = True)
    cevaplanan_mesaj = message.reply_to_message

    if len(message.command) == 1 and cevaplanan_mesaj.document:
        if cevaplanan_mesaj.document.file_name.split(".")[-1] != "py":
            await ilk_mesaj.edit("`Yalnızca python dosyası yükleyebilirsiniz..`")
            return
        eklenti_dizini = f"./apollo/bot_plugins/{cevaplanan_mesaj.document.file_name}"
        await ilk_mesaj.edit("`Eklenti Yükleniyor...`")

        if os.path.exists(eklenti_dizini):
            await ilk_mesaj.edit(f"`{cevaplanan_mesaj.document.file_name}` __eklentisi zaten mevcut!__")
            return

        try:
            await client.download_media(message=cevaplanan_mesaj, file_name=eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Eklenti Yüklendi:** `{cevaplanan_mesaj.document.file_name}`")
            return

        except Exception as hata:
            await pyro_hata(hata, ilk_mesaj)
            return

    await ilk_mesaj.edit('__Python betiği yanıtlamanız gerekmektedir__')

@Client.on_message(filters.command(['udel', 'pdel'], PREFIX) & filters.me)
async def userbot_eklenti_sil(client:Client, message:Message):

    ilk_mesaj = await message.edit("__Yükleniyor...__", disable_web_page_preview = True)

    if len(message.command) == 2:
        eklenti_dizini = f"./apollo/userbot_plugins/{message.command[1]}.py"

        if os.path.exists(eklenti_dizini):
            os.remove(eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Userbot'tan eklenti silindi:** `{message.command[1]}`")
            return

        await ilk_mesaj.edit("`Böyle bir eklenti yok`")
        return

    await ilk_mesaj.edit("`Geçerli bir eklenti adı girin!`")

@Client.on_message(filters.command(['bdel'], PREFIX) & filters.me)
async def bot_eklenti_sil(client:Client, message:Message):

    ilk_mesaj = await message.edit("__Yükleniyor...__", disable_web_page_preview = True)

    if len(message.command) == 2:
        eklenti_dizini = f"./apollo/bot_plugins/{message.command[1]}.py"

        if os.path.exists(eklenti_dizini):
            os.remove(eklenti_dizini)
            await asyncio.sleep(2)
            await ilk_mesaj.edit(f"**Asistan'dan eklenti silindi:** `{message.command[1]}`")
            return

        await ilk_mesaj.edit("`Böyle bir eklenti yok`")
        return

    await ilk_mesaj.edit("`Geçerli bir eklenti adı girin!`")

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

@Client.on_message(filters.command(['env'], PREFIX) & filters.me)
async def send_env(client:Client, message:Message):
    ilk_mesaj = await message.edit('`Hallediyorum..`', disable_web_page_preview = True)

    kullanici_adi, kullanici_id = await kullanici(message)

    env_bilgileri = f"""__İşte {kullanici_adi} » 𝓐𝓹𝓸𝓵𝓵𝓸 𝓤𝓼𝓮𝓻𝓑𝓸𝓽 🚀 Bilgileri;__
**API_ID :**
`{API_ID}`
**API_HASH :**
`{API_HASH}`
**ASISTAN(BOT)_TOKEN :**
`{BOT_TOKEN}`
**STRING_SESSION :**
`{STRING_SESSION}`
**KİMSEYLE PAYLAŞMAYINIZ!!**
`Sağlayıcı :` **@ApolloUB**"""

    await client.send_message(kullanici_id, env_bilgileri)

    await ilk_mesaj.edit(f"**{kullanici_adi} !**\n\n**Ayar bilgilerini kaydettim..**\n\n__Kayıtlı Mesajlarına Bakabilirsin..__")

CmdHelp(Path(__file__).stem).add_command("alive", None, "Bot yaşıyor mu ona bakar.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("env", None, "Size yeni bir Apollo Userbot kurmanız için gereken bilgileri verir.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("apollo", "EklentiAdi", ".uapollo komutunun kısayoludur.", ".apollo sa_as").add_userbot()
CmdHelp(Path(__file__).stem).add_command("uapollo", "EklentiAdi", "Apollo Userbot'un eklentileri hakkında bilgi öğrenmenizi sağlar.", ".uapollo sa_as").add_userbot()
CmdHelp(Path(__file__).stem).add_command("bapollo", "EklentiAdi", "Apollo Asistan'ın eklentileri hakkında bilgi öğrenmenizi sağlar.", ".bapollo sa_as").add_userbot()
CmdHelp(Path(__file__).stem).add_command("ulist", None, ".ulist komutunun kısayoludur.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("plist", None, "Apollo Userbot'un eklentilerini listeler.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("blist", None, "Apollo Asistan'ın eklentilerini listeler.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("uget", "EklentiAdi", "Apollo Userbot için yüklenmiş olan bir eklentinin kaynak kodunu getirir.", ".uget sa_as").add_userbot()
CmdHelp(Path(__file__).stem).add_command("pget", "EklentiAdi", ".uget komutunun kısayoludur.", ".pget sa_as").add_userbot()
CmdHelp(Path(__file__).stem).add_command("bget", "EklentiAdi", "Apollo Asistan için yüklenmiş olan bir eklentinin kaynak kodunu getirir.", ".bget google").add_userbot()
CmdHelp(Path(__file__).stem).add_command("uinstall", None, "Apollo Userbot için geliştirilmiş olan bir eklentiyi yanıtlayarak kurmanızı sağlar.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("pinstall", None, ".uinstall komutunun kısayoludur.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("binstall", None, "Apollo Asistan için geliştirilmiş olan bir eklentiyi yanıtlayarak kurmanızı sağlar.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("udel", "EklentiAdi", "Apollo Userbot için yüklenmiş olan bir eklentiyi silmenizi sağlar.", ".udel foobar").add_userbot()
CmdHelp(Path(__file__).stem).add_command("pdel", "EklentiAdi", ".udel komutunun kısayoludur.", ".pdel foobar").add_userbot()
CmdHelp(Path(__file__).stem).add_command("bdel", "EklentiAdi", "Apollo Asistan için yüklenmiş olan bir eklentiyi silmenizi sağlar.", ".bdel foobar").add_userbot()
CmdHelp(Path(__file__).stem).add_command("help", None, "Apollo Userbot hakkında bilgi öğrenmenizi sağlar.").add_userbot()
CmdHelp(Path(__file__).stem).add_command("yardim", None, ".help komutunun kısayoludur.").add_userbot()
