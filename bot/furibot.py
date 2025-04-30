from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .commands import FuriCommands
from config.enviroment import Enviroment

class Furibot:

    def __init__(self):

        env = Enviroment.get_enviroment()
        print(f"Running in {env} mode")

        TOKEN = getenv("BOT_TOKEN")
        if not TOKEN:
            raise ValueError("BOT_TOKEN environment variable is not set.")
        

        self.bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher()
        self.commander = FuriCommands(self.dp)

        self.commander.register_commands()

    async def start(self):
        await self.dp.start_polling(self.bot)