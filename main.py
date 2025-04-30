import asyncio
import logging
import sys
from os import getenv

from bot.furibot import Furibot

from config.installer import WebdriverInstaller

from scraping.hltv import HltvScraper

TOKEN = getenv("BOT_TOKEN")

bot = Furibot()

driver = WebdriverInstaller.install_webdriver("firefox")
scraper = HltvScraper(base="https://www.hltv.org/", webdriver=driver)

if __name__ == "__main__":

    scraper.opening_base()

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(bot.start())