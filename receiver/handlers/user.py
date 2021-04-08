from telethon import events

from config import bot


@bot.on(events.NewMessage)
async def any_msg_handler(event):
    await event.reply('Hey!')
