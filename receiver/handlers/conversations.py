from telethon import events

from api_driver import GatewayAPIDriver
from config import bot


@bot.on(events.NewMessage(pattern='/familiarize'))
async def familiarize_conv_handler(event) -> None:
    chat_id = event.peer_id

    async with bot.conversation(chat_id) as conv:
        await conv.send_message('Hi! Please tell me your name')
        name = (await conv.get_response()).raw_text

        while not any(x.isalpha() for x in name):
            await conv.send_message("Your name didn't have any letters! Try again")
            name = (await conv.get_response()).raw_text

        await conv.send_message('Nice to meet you {}!'.format(name))

    await GatewayAPIDriver.tg_user_create(name, chat_id.user_id)
