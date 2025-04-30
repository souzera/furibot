class Enviroment:

    @staticmethod
    def get_enviroment():
        import os

        env = {
            "bot_token": os.getenv("BOT_TOKEN"),
            "gemini_key": os.getenv("GEMINI_KEY"),
        }

        return env