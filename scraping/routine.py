from time import sleep

class HltvRoutine:

    def __init__(self, scraper):
        self.scraper = scraper

    def run(self):
        self.scraper.opening_base()
        sleep(5)
        
        self.scraper.allow_cookies()
        sleep(5)
        
        self.scraper.opening_ranking()
        sleep(5)

        self.scraper.collect_ranking()
        sleep(5)

        


