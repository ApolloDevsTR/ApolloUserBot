# Thanks Seden UserBot - TeamDerUntergang
# Thanks Asena UserBot - yusufusta

from git import Repo
from os import path, environ, remove, execle
import asyncio
import sys
from apollo.lib.CmdHelp import CmdHelp
from pathlib import Path
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from apollo import REPO_URL, PREFIX
from pyrogram import Client, filters
from pyrogram.types import Message

requirements_path = path.join(path.dirname(
    path.dirname(path.dirname(__file__))), 'requirements.txt')


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@Client.on_message(filters.command(['update'], PREFIX) & filters.me)
async def guncelle(client: Client, message: Message):
    await message.edit("`Güncellemeler denetleniyor...`")
    now_update = False
    force_update = False
    if len(message.command) == 2:
        if message.command[1] == "now":
            now_update = True
        elif message.command[1] == "force":
            force_update = True
    try:
        txt = "`Güncelleme başarısız oldu! Bazı sorunlarla karşılaştım.`\n\n**LOG:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        repo = Repo()
        await message.edit(f'{txt}\n`{error} klasörü bulunamadı.`')
        repo.__del__()
        return
    except GitCommandError as error:
        await message.edit(f'{txt}\n`⚠️ Git hatası ⚠️\n{error}`')
        repo = Repo()
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        repo = Repo.init()
        origin = repo.create_remote("upstream", REPO_URL)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br == 'dev':
        await message.edit("**[UPDATER]:**` Sanırım Apollo UserBot'un `dev` yani geliştirme branchını kullanıyorsun ve bu branch pek sağlıklı çalışmayabilir lütfen `main` branchına geçiniz.")
        repo.__del__()
        return
    elif ac_br != 'main':
        await message.edit("**[UPDATER]:**` Sanırım Apollo UserBot'u modifiye ettin ve `main`'den farklı bir branch kullanıyorsun.\nBu durum güncelleyicinin kafasını karıştırıyor.\nMadem botu modifiye ettin bunu düzeltmeyi de biliyorsundur. İyi şanslar :)")
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', REPO_URL)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog and not force_update:
        await message.edit("**✅  Şu an en güncel durumdayım!** \n**📡 Branch: {}**".format(ac_br))
        repo.__del__()
        return

    if not now_update and not force_update:
        changelog_str = "**{} için yeni güncelleme mevcut!\n\nDeğişiklikler:**\n`{}`".format(
            ac_br, changelog)
        if len(changelog_str) > 4096:
            await message.edit("`Değişiklik listesi çok büyük, dosya olarak görüntülemelisin.`")
            file = open("degisiklikler.txt", "w+")
            file.write(changelog_str)
            file.close()
            await client.send_document(
                message.chat_id,
                "degisiklikler.txt",
                reply_to_message_id=message.id,
            )
            remove("degisiklikler.txt")
        else:
            await message.edit(changelog_str)
        await client.send_message(message.chat.id, "`Güncellemeyi yapmak için \".update now\" komutunu kullan.`")
        return

    if force_update:
        await message.edit("`Güncel userbot kodu zorla eşitleniyor...`")
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await update_requirements()
        await message.edit("`Güncel userbot kodu zorla eşitlendi`")
        args = [sys.executable, "-m", "apollo"]
        execle(sys.executable, *args, environ)
        return
    elif now_update:
        await message.edit("❤️**Durum**: __Güncelleniyor..\n\n💌 UserBot'unuzun daha iyi olacağınıza emin olabilirsiniz :) Bu işlem maksimum 10 dakika sürmektedir.__")
        try:
            ups_rem.pull(ac_br)

        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await update_requirements()
    await message.edit("❤️**Durum:** __Güncelleme başarıyla tamamlandı!\n\n🔄 Yeniden başlatılıyor...__")
    args = [sys.executable, "-m", "apollo"]
    execle(sys.executable, *args, environ)
    return

myCmdHelp = CmdHelp(Path(__file__).stem)
myCmdHelp.add_command("update now", usage="UserBot'unuzu günceller.")
myCmdHelp.add_command("update force", usage="UserBot'unuzu ZORLA günceller.")
myCmdHelp.add_command("update", usage="UserBot'a yeni gelen güncellemeleri gösterir.")
myCmdHelp.add_warning("`.update force` komutunu ne yaptığınızı bilmediğiniz sürece kullanmamanız şiddetle önerilir çünkü veri kaybına yol açabilir.")
myCmdHelp.add_userbot()