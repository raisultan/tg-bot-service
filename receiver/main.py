from config import bot

from handlers import *


if __name__ == '__main__':
    bot.start()
    print('Bot is running!')
    bot.run_until_disconnected()
