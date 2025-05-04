import os
import sys
import asyncio
import logging

from os import getenv

from bot.furibot import Furibot

from config.installer import WebdriverInstaller
from config.enviroment import Enviroment

from scraping.hltv import HltvScraper
from scraping.routine import HltvRoutine
from scraping.teams import *

from services.pandascore import PandascoreAdapter

TOKEN = getenv("BOT_TOKEN")

bot = Furibot()

driver = WebdriverInstaller.install_webdriver("firefox")

scraper = HltvScraper(base="https://www.hltv.org/", webdriver=driver)
routine = HltvRoutine(scraper, team=FURIA)

api = PandascoreAdapter(token=Enviroment.get_enviroment()["pandascore_key"], game="csgo")


if __name__ == "__main__":

    api.list_teams()

    # TODO: thread for schedule daily scraping
    routine.run()

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(bot.start())