from selenium.webdriver.common.by import By

from util.generator import Generator

class HltvScraper:

    def __init__(self, base: str, webdriver):
        self.base = base
        self.driver = webdriver

    def opening_base(self):
        print(f"Opening {self.base}...")

        print(type(self.driver))

        self.driver.get(self.base)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def click_button(self, button_xpath: str):
        print(f"Clicking button with xpath: {button_xpath}")
        button = self.driver.find_element("xpath", button_xpath)
        button.click()
        print("Button clicked.")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def allow_cookies(self):
        print("Allowing cookies...")
        button_xpath = '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
        self.click_button(button_xpath)
        print("Cookies allowed.")
        self.driver.implicitly_wait(10)


    def opening_ranking(self):
        print("Opening ranking page...")
        ranking_url = f"{self.base}/ranking/teams"
        self.driver.get(ranking_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("Ranking page opened.")
        self.driver.implicitly_wait(10)

    
    def collect_ranking(self):
        try:
            elements = self.driver.find_elements(By.CLASS_NAME, "ranked-team")

            elements[0].click()

            teams = []
            for team in elements:
                team_name = team.find_element(By.CLASS_NAME, "name").text
                team_rank = team.find_element(By.CLASS_NAME, "position").text
                team_points = team.find_element(By.CLASS_NAME, "points").text

                # TODO: Error on trying to get players of expanded container teams
                
                team_players = team.find_elements(By.CLASS_NAME, "rankingNicknames")
                team_players = [player.text for player in team_players]
                
                
                teams.append({
                    "rank": team_rank,
                    "name": team_name,
                    "points": int(team_points.replace(" pts", "").replace("(", "").replace(")", "")),
                    "players": team_players
                })
            
            Generator.save_as_dataframe(data=teams, filename="static/ranking_hltv")
            print("Ranking collected successfully.")
        except Exception as e:
            print(f"Error collecting ranking: {e}")