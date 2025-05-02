import pandas as pd

class Generator:

    @staticmethod
    def save_as_dataframe(data, filename):
        df = pd.DataFrame(data)
        df.to_csv(f"{filename}.csv", index=False)
        df.to_json(f'{filename}.json', orient='records', lines=True)