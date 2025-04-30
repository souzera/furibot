import asyncio
import logging
import sys
from os import getenv

from bot.furibot import Furibot

TOKEN = getenv("BOT_TOKEN")

bot = Furibot()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(bot.start())