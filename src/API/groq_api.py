from groq import Groq

from . import api_key
from utils.color_text import color_text


class Groq_API:
    def __init__(self, model_name: str = ""):
        self.client = Groq(api_key=api_key.GROQ_API_KEY)
        self.chat_history = []
        self.model_name = model_name

    def chat(self, user_input: str):
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
            messages=self.chat_history, model=self.model_name
        )
        self.chat_history.append(
            {"role": "assistant", "content": response.choices[0].message.content}
        )
        return response.choices[0].message.content

    def call_groq_api(self):
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
            response = self.chat(user_input)
            print()
            print(color_text("(assistant) >>> ", "blue") + response)
            print()

        return self.chat_history


if __name__ == "__main__":
    import sys

    print(sys.path)
    groq_api = Groq_API()
    groq_api.call_groq_api()
