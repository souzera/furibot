import pandas as pd

from config.enviroment import Enviroment

from aiogram import Dispatcher, html
from aiogram.filters import CommandStart, Command

from ai.agent import AiAgent
from google import genai

class FuriCommands:

    def __init__(self, dp: Dispatcher):
        self.dp = dp

        GEMINI_KEY = Enviroment.get_enviroment()['gemini_key']
        client = genai.Client(api_key=GEMINI_KEY)

        self.agent = AiAgent("GEMINI", 'gemini-1.5-flash', client)

    def command_start_handler(self, message):
        return message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    
    def command_help_handler(self, message):
        return message.answer("I can help you with the following commands:\n\n" +
            "/ai <question> - Ask me anything!\n" +
            "/echo <message> - Echo back your message.\n" +
            "/next - Get the next match of FURIA.\n" +
            "/last - Get the last match of FURIA.\n" +
            "/ranking - Get the current HLTV ranking of FURIA.\n" +
            "/roster - Get the current roster of FURIA.\n")
    
    def echo_handler(self, message):
        try:
            return message.send_copy(chat_id=message.chat.id)
        except TypeError:
            return message.answer("Nice try!")
        
    def ai_handler(self, message):
        print(f"Received message: {message.text}")

        question = message.text.split(" ", 1)[1] if " " in message.text else ""

        response = self.agent.generate_response(question)
        print(f"Generated response: {response}")

        return message.answer(response.text)
    
    def next_match_handler(self, message):

        matches = pd.read_csv("static/csv/matches_hltv.csv")

        upcoming_matches = matches[matches["type"] == "upcoming"]

        response = f"A proxima partida da FURIA será contra {upcoming_matches.iloc[0]['team_2']} no dia {upcoming_matches.iloc[0]['date']}. Para mais detalhes, acesse: {upcoming_matches.iloc[0]['url']}"
        
        return message.answer(response)

    def last_match_handler(self, message):
        matches = pd.read_csv("static/csv/matches_hltv.csv")

        results = matches[matches["type"] == "result"]

        response = f"A ultima partida da FURIA foi contra {results.iloc[0]['team_2']} no dia {results.iloc[0]['date']}, com o placar de {results.iloc[0]['score_1']}x{results.iloc[0]['score_2']} {str(results.iloc[0]['team_2']).upper()}. \n\nPara mais detalhes, acesse: {results.iloc[0]['url']}"
        
        return message.answer(response)
    
    def current_hltv_ranking_handler(self, message):
        ranking = pd.read_csv("static/csv/ranking_hltv.csv")

        furia_placement = ranking[ranking["name"] == "FURIA"]

        response = f"A FURIA está na posição {furia_placement['rank'].values[0]} com {furia_placement['points'].values[0]} pontos."
        return message.answer(response)
    
    def roster_handler(self, message):
        return message.answer("Atualmentee, integram a FURIA \n\n" +
            "FALLEN\n" +
            "KSCERATO\n" +
            "YUURIH\n" +
            "YEKINDAR\n" +
            "MOLODOY\n" +
            "\n" +
            "Coach. SIDDE\n")

    def register_commands(self):
        self.dp.message.register(self.command_start_handler, CommandStart())
        self.dp.message.register(self.echo_handler, Command("echo"))

        self.dp.message.register(self.ai_handler, Command("ai"))
        self.dp.message.register(self.next_match_handler, Command("next"))
        self.dp.message.register(self.last_match_handler, Command("last"))
        self.dp.message.register(self.current_hltv_ranking_handler, Command("ranking"))
        self.dp.message.register(self.roster_handler, Command("roster"))
