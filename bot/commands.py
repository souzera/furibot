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

    def register_commands(self):
        self.dp.message.register(self.command_start_handler, CommandStart())
        self.dp.message.register(self.echo_handler, Command("echo"))

        self.dp.message.register(self.ai_handler, Command("ai"))