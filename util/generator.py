import pandas as pd

class Generator:

    @staticmethod
    def save_as_json(data, filename):
        pd.DataFrame(data).to_json(f'{filename}.json', orient='records', lines=True)

    @staticmethod
    def save_as_csv(data, filename):
        pd.DataFrame(data).to_csv(f"{filename}.csv", index=False)