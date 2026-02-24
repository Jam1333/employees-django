import ollama
import project.settings

class OllamaService:
    def __init__(self):
        self.client = ollama.Client(host=project.settings.OLLAMA_URL)
        
    def get_response(self, prompt):
        response = self.client.chat(model=project.settings.OLLAMA_MODEL, messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ])
        
        return response["message"]["content"]