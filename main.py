from os import getenv

from bot.furibot import Furibot

from config.installer import WebdriverInstaller

from scraping.hltv import HltvScraper
from scraping.routine import HltvRoutine
from scraping.teams import *

TOKEN = getenv("BOT_TOKEN")

bot = Furibot()

driver = WebdriverInstaller.install_webdriver("firefox")

scraper = HltvScraper(base="https://www.hltv.org/", webdriver=driver)
routine = HltvRoutine(scraper, team=FURIA)

if __name__ == "__main__":

    routine.run()

    # ogging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # asyncio.run(bot.start())