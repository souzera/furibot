from time import sleep
from .hltv import HltvScraper

class HltvRoutine:

    def __init__(self, scraper: HltvScraper, team=None):
        self.scraper = scraper
        self.team = team

    def hltv_ranking_routine(self):
        self.scraper.opening_ranking()
        sleep(5)

    def matches_routine(self):

        if self.team:
            self.scraper.open_matches(self.team)
            sleep(5)
            self.scraper.collect_matches()
            sleep(5)


    def player_stats_routine(self):
        pass

    def upcoming_events_routine(self):
        pass

    def roster_routine(self):
        pass

    def achievements_routine(self):
        pass

    def news_routine(self):
        pass

    def last_matches_routine(self):
        pass

    def run(self):
        self.scraper.opening_base()
        sleep(5)
        
        self.scraper.allow_cookies()
        sleep(5)

        if self.team:
            self.matches_routine()
            sleep(5)

        self.scraper.driver.quit()
        print("Driver closed.")

        


