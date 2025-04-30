from os import getenv

from aiogram import Dispatcher, html
from aiogram.filters import CommandStart

from ai.agent import AiAgent
from google import genai

class FuriCommands:

    def __init__(self, dp: Dispatcher):
        self.dp = dp
        
        KEY = getenv("GEMINI_KEY")
        if not KEY:
            raise ValueError("GEMINI_KEY environment variable is not set.")
        

        client = genai.Client(api_key=getenv("GEMINI_KEY"))

        self.agent = AiAgent("GEMINI", 'gemini-1.5-flash', client)

    def command_start_handler(self, message):
        return message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    
    def echo_handler(self, message):
        try:
            return message.send_copy(chat_id=message.chat.id)
        except TypeError:
            return message.answer("Nice try!")
        
    def ai_handler(self, message):
        response = self.agent.generate_response(message.text)
        return message.answer(response)

    def register_commands(self):
        self.dp.message.register(self.command_start_handler, CommandStart())
        self.dp.message.register(self.echo_handler)

        self.dp.message.register(self.ai_handler, commands=["ai"])