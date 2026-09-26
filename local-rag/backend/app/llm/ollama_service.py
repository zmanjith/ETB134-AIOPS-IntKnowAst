import os
import requests


class OllamaService:

    def __init__(self):

        self.host = os.getenv("OLLAMA_HOST", "localhost")
        self.port = os.getenv("OLLAMA_PORT", "11434")
        self.model = os.getenv("OLLAMA_MODEL", "llama3.2")

        self.url = f"http://{self.host}:{self.port}/api/generate"

    def generate(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            self.url,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]