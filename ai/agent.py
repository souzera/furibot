from google import genai

class AiAgent:

    def __init__(self, name, model, llm: genai.Client):
        self.name = name
        self.model = model
        self.llm = llm

    def generate_response(self, prompt):
        return self.llm.models.generate_content(
            model=self.model,
            contents=[prompt]
        )

    