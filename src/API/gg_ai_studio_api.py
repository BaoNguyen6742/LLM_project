import google.generativeai as genai
from . import api_key
from utils.color_text import color_text
import os

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"


class GG_AI_Studio_API:
    def __init__(self, model_name: str = ""):
        genai.configure(api_key=api_key.GG_API_KEY, transport="rest")
        model = genai.GenerativeModel(model_name)
        self.model_name = model_name
        self.chat_session = model.start_chat()

    def chat(self, user_input: str) -> str:
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
        respond = self.chat_session.send_message(user_input)
        return respond.text

    def call_gg_api(self) -> list[dict]:
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
            response = self.chat(user_input)
            print()
            print(color_text("(assistant) >>> ", "blue") + response)
        return self.chat_session.history


if __name__ == "__main__":
    gg_api = GG_AI_Studio_API("gemini-1.5-flash")
    gg_api.call_gg_api()
