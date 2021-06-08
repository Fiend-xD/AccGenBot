from AccGenBot import AccGen
from AccGenBot.verify import verify
from telethon import events, Button
from Configs import Config

@AccGen.on(events.callbackquery.CallbackQuery(data="gen"))
async def gen(gen):
     check = await verify(Config.CHANNEL_US, gen, AccGen)
     if check is False:
       await gen.reply("**♢ Join All Below Channel Then /start Again To Use Me ♢**", buttons=[
       [Button.url("★ Join Channel ★", "https://t.me/NETFLIX_PREMIUM_ZONE")],
       [Button.url("★ Join Channel ★", "{}".format(Config.CHANNEL_URL))],
       [Button.url("★ Join Channel ★", "https://t.me/Avengers_Era")]
       ])
       return

     TEXT = """
**Hey {}**

☩ Choose The Account You Wanna Generate ☩
""".format(gen.sender.first_name)

     await gen.edit(TEXT, buttons=[
     [Button.inline("Zee5", data="zee5"), Button.inline("Voot", data="voot")],
     [Button.inline("AltBalaji", data="alt"), Button.inline("Spotify", data="sp")],
     [Button.url("✘ Support ✘", "https://t.me/Fiend_Army")]
     ])
