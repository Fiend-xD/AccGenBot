from AccGenBot import AccGen
from AccGenBot.verify import verify
from telethon import events, Button
import random
from Configs import Config

@AccGen.on(events.callbackquery.CallbackQuery(data="zee5"))
async def zee5(event):
    check = await verify(Config.CHANNEL_US, event, AccGen)
    if check is False:
       await event.reply("**Join my channel to use me:)**", buttons=[
       [Button.url("✘ Support ✘", "https://t.me/Fiend_Army")]
       ])
       return
    with open('zee5.txt') as k:
      hits = k.read().splitlines()
      combo = random.choice(hits)
      email, password = combo.split(":")
    TEXT = f"""
<b>Generated Zee5 Acc</b>

<b>Combo:</b> <code>{email}:{password}</code>
<b>Email:</b> <code>{email}</code>
<b>Password:</b> <code>{password}</code>

<b>Generated By: @{event.sender.username}</b>
<b>User-ID: {event.sender_id}</b>
"""

    await event.edit(TEXT, parse_mode="HTML", buttons=[[Button.inline("Back", data="gen")]
    ])

@AccGen.on(events.callbackquery.CallbackQuery(data="voot"))
async def voot(event):
    check = await verify(Config.CHANNEL_US, event, AccGen)
    if check is False:
       await event.reply("**Join my channel to use me:)**", buttons=[
       [Button.url("Join Channel", "{}".format(Config.CHANNEL_URL))]
       ])
    with open('voot.txt') as k:
      hits = k.read().splitlines()
      combo = random.choice(hits)
      email, password = combo.split(":")
    TEXT = f"""
<b>Generated Voot Acc</b>

<b>Combo:</b> <code>{email}:{password}</code>
<b>Email:</b> <code>{email}</code>
<b>Password:</b> <code>{password}</code>

<b>Generated By: @{event.sender.username}</b>
<b>User-ID: {event.sender_id}</b>
"""

    await event.edit(TEXT, parse_mode="HTML", buttons=[[Button.inline("Back", data="gen")]
    ])

@AccGen.on(events.callbackquery.CallbackQuery(data="alt"))
async def alt(event):
    check = await verify(Config.CHANNEL_US, event, AccGen)
    if check is False:
       await event.reply("**Join my channel to use me:)**", buttons=[
       [Button.url("Join Channel", "{}".format(Config.CHANNEL_URL))]
       ])
       return
    with open('alt.txt') as k:
      hits = k.read().splitlines()
      combo = random.choice(hits)
      email, password = combo.split(":")
    TEXT = f"""
<b>Generated AltBalaji Acc</b>

<b>Combo:</b> <code>{email}:{password}</code>
<b>Email:</b> <code>{email}</code>
<b>Password:</b> <code>{password}</code>

<b>Generated By: @{event.sender.username}</b>
<b>User-ID: {event.sender_id}</b>
"""

    await event.edit(TEXT, parse_mode="HTML", buttons=[[Button.inline("Back", data="gen")]
    ])

@AccGen.on(events.callbackquery.CallbackQuery(data="sp"))
async def zee5(event):
    check = await verify(Config.CHANNEL_US, event, AccGen)
    if check is False:
       await event.reply("**Join my channel to use me:)**", buttons=[
       [Button.url("Join Channel", "{}".format(Config.CHANNEL_URL))]
       ])
       return
    with open('sp.txt') as k:
      hits = k.read().splitlines()
      combo = random.choice(hits)
      email, password = combo.split(":")
    TEXT = f"""
<b>Generated Spotify Acc</b>

<b>Combo:</b> <code>{email}:{password}</code>
<b>Email:</b> <code>{email}</code>
<b>Password:</b> <code>{password}</code>

<b>Generated By: @{event.sender.username}</b>
<b>User-ID: {event.sender_id}</b>
"""

    await event.edit(TEXT, parse_mode="HTML", buttons=[[Button.inline("Back", data="gen")]
    ])
