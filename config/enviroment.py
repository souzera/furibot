import os
from dotenv import load_dotenv

class Enviroment:

    @staticmethod
    def get_enviroment():

        load_dotenv()

        env = {
            "bot_token": os.getenv("BOT_TOKEN"),
            "gemini_key": os.getenv("GEMINI_KEY"),
            "pandascore_key": os.getenv("PANDASCORE_KEY"),
        }

        return env