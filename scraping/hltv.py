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
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()
        print("Button clicked.")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def allow_cookies(self):
        try:
            print("Allowing cookies...")
            button_xpath = '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
            self.click_button(button_xpath)
            print("Cookies allowed.")
            self.driver.implicitly_wait(10)
        except Exception as e:
            print(f"Error allowing cookies: {e}")
            return


    def opening_ranking(self):
        print("Opening ranking page...")
        ranking_url = f"{self.base}/ranking/teams"
        self.driver.get(ranking_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("Ranking page opened.")
        self.driver.implicitly_wait(10)

    
    def collect_ranking(self):

        def collect_players(team):
            team_players = team.find_elements(By.CLASS_NAME, "rankingNicknames")
            team_players = [player.text for player in team_players]

            if "" in team_players:
                team_players = team.find_elements(By.CLASS_NAME, "nick")
                team_players = [player.text for player in team_players]

            return team_players

        try:
            elements = self.driver.find_elements(By.CLASS_NAME, "ranked-team")

            teams = []
            for team in elements:
                team_name = team.find_element(By.CLASS_NAME, "name").text
                team_rank = team.find_element(By.CLASS_NAME, "position").text
                team_points = team.find_element(By.CLASS_NAME, "points").text
                
                teams.append({
                    "rank": team_rank,
                    "name": team_name,
                    "points": int(team_points.replace(" HLTV points", "").replace("(", "").replace(")", "")),
                    "players": collect_players(team)
                })
            
            Generator.save_as_csv(data=teams, filename="ranking_hltv")
            Generator.save_as_json(data=teams, filename="ranking_hltv")
            print("Ranking collected successfully.")
        except Exception as e:
            print(f"Error collecting ranking: {e}")

    def open_matches(self, team):
        print("Opening matches page...")
        matches_url = f"{self.base}team/{team}#tab-matchesBox"
        self.driver.implicitly_wait(10)
        self.driver.get(matches_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("Matches page opened.")
        self.driver.implicitly_wait(10)

    
    def collect_matches(self):

        def score_tratament(score):
            if score == "-":
                return 0
            else:
                return int(score)
            
            

        try:
            elements = self.driver.find_elements(By.CLASS_NAME, "match-table")

            matches = []

            for table in elements:
                match_elements = table.find_elements(By.CLASS_NAME, "team-row")

                for match in match_elements:
                    teams = match.find_elements(By.CLASS_NAME, "team-name")
                    
                    try:
                        match_url = match.find_element(By.CLASS_NAME, "matchpage-button-cell a").get_attribute("href")
                    except:
                        match_url = "No URL"

                    if match_url == "No URL":
                        try:
                            match_url = match.find_element(By.CLASS_NAME, "stats-button-cell a").get_attribute("href")
                        except:
                            match_url = "No URL"

                    score = match.find_elements(By.CLASS_NAME, "score")

                    date = match.find_element(By.CLASS_NAME, "date-cell span").text

                    match_item = {
                        "date": date,
                        "team_1": teams[0].text,
                        "score_1": score_tratament(score[0].text),
                        "team_2": teams[1].text,
                        "score_2": score_tratament(score[1].text),
                        "url": match_url
                    }

                    match_item["type"] = "upcoming" if match_item["score_1"] == 0 and match_item["score_2"] == 0 else "result"
                    
                    matches.append(match_item)

            Generator.save_as_csv(data=matches, filename="matches_hltv")
            Generator.save_as_json(data=matches, filename="matches_hltv")
            print("Matches collected successfully.")


                
        except Exception as e:
            print(f"Error collecting matches: {e}")
            return