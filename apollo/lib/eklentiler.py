from os import listdir

def userbot_eklentileri(liste=False):
    if liste:
        tum_eklentiler = []
        
        for dosya in listdir("./apollo/userbot_plugins/"):
            if not dosya.endswith(".py") or dosya.startswith("_"):
                continue
            tum_eklentiler.append(f"🚀 {dosya.replace('.py','')}")
    else:
        tum_eklentiler = ""

        for dosya in listdir("./apollo/bot_plugins/"):
            if not dosya.endswith(".py") or dosya.startswith("_"):
                continue
            tum_eklentiler += f"🚀 `{dosya.replace('.py','')}`\n"

    return tum_eklentiler


def bot_eklentileri(liste=False):
    if liste:
        tum_eklentiler = []

        for dosya in listdir("./apollo/bot_plugins/"):
            if not dosya.endswith(".py") or dosya.startswith("_"):
                continue
            tum_eklentiler.append(f"🚀 {dosya.replace('.py','')}")
    else:
        tum_eklentiler = ""

        for dosya in listdir("./apollo/bot_plugins/"):
            if not dosya.endswith(".py") or dosya.startswith("_"):
                continue
            tum_eklentiler += f"🚀 `{dosya.replace('.py','')}`\n"

    return tum_eklentiler