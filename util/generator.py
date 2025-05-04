import pandas as pd

BASE_PATH = "static/"

class Generator:


    @staticmethod
    def save_as_json(data, filename):
        pd.DataFrame(data).to_json(f'{BASE_PATH}json/{filename}.json', orient='records')

    @staticmethod
    def save_as_csv(data, filename):
        pd.DataFrame(data).to_csv(f"{BASE_PATH}csv/{filename}.csv", index=False)