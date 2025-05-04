import requests

API_ROOT =  "https://api.pandascore.co/"

class PandascoreAdapter:

    def __init__(self, token: str, game: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }
        self.game = game

    def list_teams(self, **kwargs):
        url = f"{API_ROOT}{self.game}/teams"
        response = requests.get(url, headers=self.headers, params=kwargs)
        print(response.json())

        return response.text
    

    # TODO: statistic functions
    # TODO: player functions
    # TODO: current matches functions