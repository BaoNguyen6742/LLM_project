import google.generativeai as genai

from typing import Iterator

from ..utils.color_text import color_text
from ..utils.text_utils import clear_screen

from . import api_key


class GG_AI_Studio_API:
    def __init__(self, model_name: str = ""):
        genai.configure(api_key=api_key.GG_API_KEY, transport="rest")
        model = genai.GenerativeModel(model_name)
        self.model_name = model_name
        self.chat_session = model.start_chat()
        clear_screen()
        print(
            color_text(
                f'You are chatting with {model_name} model. Type "<exit>" to exit.\n\n',
                "yellow",
            )
        )
        self.stream = True

    def chat(self, user_input: str) -> str | Iterator[str]:
        """
        Chat with the assistant.
        
        Behavior
        --------
        Chat with the assistant using the GG AI Studio API.
        
        Parameters
        ----------
        - user_input : `str` \\
            The input from the user.
        - model : `str`. Optional, by default "" \\
            The model to be used for the chat.
        
        Returns
        -------
        - response.txt : `str` \\
            The response from the assistant.
        """
        respond = self.chat_session.send_message(user_input, stream=self.stream)
        if self.stream:
            return respond
        else:
            return respond.text

    def call_api(self) -> list[dict]:
        """
        Call the GG AI Studio API to chat with the assistant.
        
        Behavior
        --------
        Initialize the GG AI Studio client with the API key and chat with the assistant.
        
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
            print(color_text("(assistant) >>> ", "blue"), end="")
            response = self.chat(user_input)
            if self.stream:
                for chunk in response:
                    print(color_text(chunk.text, "blue"), end="")
            else:
                print(response)
            print()
        return self.chat_session.history


if __name__ == "__main__":
    gg_api = GG_AI_Studio_API("gemini-1.5-flash")
    gg_api.call_api()
