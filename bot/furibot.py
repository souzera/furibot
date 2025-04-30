
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .commands import FuriCommands
from config.enviroment import Enviroment

class Furibot:

    def __init__(self):

        env = Enviroment.get_enviroment()
        print(f"Running in {env} mode")
        

        self.bot = Bot(token=env['bot_token'], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher()
        self.commander = FuriCommands(self.dp)

        self.commander.register_commands()

    async def start(self):
        await self.dp.start_polling(self.bot)