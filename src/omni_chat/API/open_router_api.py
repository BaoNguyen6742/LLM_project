import json

import requests
from openai import OpenAI

from . import api_key
from ..utils.color_text import color_text
from ..utils.text_utils import clear_screen


class OpenRouter_API:
    def __init__(self, model_name: str = ""):
        self.model_name = model_name
        self.chat_history = []
        self.stream = True
        clear_screen()
        print(
            color_text(
                f'You are chatting with {model_name} model. Type "<exit>" to exit.\n\n',
                "yellow",
            )
        )
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key.OPENROUTER_API_KEY,
        )

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
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.chat_history,
            stream=self.stream,
        )
        if self.stream:
            return response
        else:
            return response.choices[0].message.content

    def call_api(self) -> list[dict]:
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
            print()
            response_text = ""
            print(color_text("(assistant) >>> ", "blue"), end="")
            response = self.chat(user_input)
            if self.stream:
                for chunk in response:
                    response_text += chunk.choices[0].delta.content
                    print(color_text(chunk.choices[0].delta.content, "blue"), end="")
            else:
                response_text = response.choices[0].message.content
                print(color_text(response_text, "blue"), end="")
            self.chat_history.append({"role": "assistant", "content": response_text})
            print("\n")
        return self.chat_history


if __name__ == "__main__":
    open_router_instance = OpenRouter_API(model_name="gpt-3.5-turbo")
    open_router_instance.call_api()
