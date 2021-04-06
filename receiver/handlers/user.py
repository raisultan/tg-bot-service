from pyrogram import filters

from config.bot import bot


@bot.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply_text(message.text)
