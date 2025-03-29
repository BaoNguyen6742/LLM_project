from groq import Groq

from typing import Iterator

from . import api_key
from ..utils.color_text import color_text
from ..utils.text_utils import clear_screen


class Groq_API:
    def __init__(self, model_name: str = ""):
        self.client = Groq(api_key=api_key.GROQ_API_KEY)
        self.chat_history = []
        self.model_name = model_name
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
        Chat with the assistant using the GROQ API.
        
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
            messages=self.chat_history, model=self.model_name, stream=self.stream
        )
        if self.stream:
            return response
        else:
            return response.choices[0].message.content

    def call_api(self):
        """
        Call the GROQ API to chat with the assistant.
        
        Behavior
        --------
        Initialize the GROQ client with the API key and chat with the assistant.
        
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
            respont_text = ""
            print(color_text("(assistant) >>> ", "blue"), end="")
            response = self.chat(user_input)
            if self.stream:
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        respont_text += chunk.choices[0].delta.content
                        print(
                            color_text(chunk.choices[0].delta.content, "blue"), end=""
                        )
            else:
                respont_text = response

            self.chat_history.append({"role": "assistant", "content": respont_text})
            print("\n")

        return self.chat_history


if __name__ == "__main__":
    import sys

    print(sys.path)
    groq_api = Groq_API()
    groq_api.call_api()
