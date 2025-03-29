import json

import requests

from . import api_key
from utils.color_text import color_text


class OpenRouter_API:
    def __init__(self, model_name: str = ""):
        self.model_name = model_name
        self.chat_history = []

    def chat(self, user_input: str) -> str:
        """
        Chat with the assistant.
        
        Behavior
        --------
        Chat with the assistant using the Open Router API.
        
        Parameters
        ----------
        - user_input : `str` \\
            The input from the user.
        - model : `str`. Optional, by default "" \\
            The model to be used for the chat.
        
        Returns
        -------
        - response : `str` \\
            The response from the assistant.
        """
        self.chat_history.append({"role": "user", "content": user_input})
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key.OPENROUTER_API_KEY}",
            },
            data=json.dumps({"model": self.model_name, "messages": self.chat_history}),
        )

        return response.json()["choices"][0]["message"]["content"]

    def call_open_router_api(self) -> list[dict]:
        """
        Call the Open Router API to chat with the assistant.
        
        Behavior
        --------
        Initialize the Open Router client with the API key and chat with the assistant.
        
        Parameters
        ----------
        - model : `str`. Optional, by default "" \\
            The model to be used for the chat.,
            
        Returns
        -------
        - chat_history  : `list[dict]` \\
            The chat history.
        """
        while True:
            user_input = input(color_text("(user) >>> ", "green"))
            if user_input == "<exit>":
                break
            response = self.chat(user_input)
            self.chat_history.append({"role": "assistant", "content": response})
            print()
            print(color_text("(assistant) >>> ", "blue") + response)
            print("")
        return self.chat_history


if __name__ == "__main__":
    open_router_instance = OpenRouter_API(model_name="gpt-3.5-turbo")
    open_router_instance.call_open_router_api()
