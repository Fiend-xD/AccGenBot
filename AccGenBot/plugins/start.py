from AccGenBot import AccGen
from telethon import events, Button
from AccGenBot.verify import verify
from Configs import Config

@AccGen.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):
    await AccGen.send_message(Config.LOGS_CHAT, f"Bot Started By {event.sender.first_name}")
    check = await verify(Config.CHANNEL_US, event, AccGen)
    if check is False:
       await event.reply("**Join All Below Channel Then /start Again To Use Me..!!:)**", buttons=[
       [Button.url("★ Join Channel ★", "https://t.me/NETFLIX_PREMIUM_ZONE")],
       [Button.url("★ Join Channel ★", "{}".format(Config.CHANNEL_URL))],
       [Button.url("★ Join Channel ★", "https://t.me/Avengers_Era")]
       ])
       return

    if event.is_group:
       await event.reply("**Sorry, I Work in PM only.**\n__I am leaving this chat...__")
       await AccGen.delete_dialog(event.chat_id)
       return

    START_TEXT = """
**Hey {}
Welcome To 𝗠𝗨𝗟𝗧𝗜 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 
✿ Here You Can Generate The Accounts You Want ✿
Press The Button Generate To Get Accounts Lists ☈**
""".format(event.sender.first_name)

    await event.reply(START_TEXT, buttons=[
    [Button.inline("Generate Accounts", data="gen")],
    [Button.url("✘ Support ✘", "https://t.me/Fiend_Army")]
    ])
