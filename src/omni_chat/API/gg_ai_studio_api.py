import os
from pprint import pprint

from google import genai

from ..utils.color_text import color_text
from . import api_key

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"


class GG_AI_Studio_API:
    def __init__(self, model_name: str = "", stream: bool = False):
        self.model_name = model_name
        self.stream = stream
        client = genai.Client(api_key=api_key.GG_API_KEY)
        self.chat_session = client.chats.create(model=self.model_name)

    def call_llm_api(self, user_input: str) -> str:
        """
        Chat with the assistant.
        
        Behavior
        --------
        Chat with the assistant using the GG AI Studio API.
        
        Parameters
        ----------
        - user_input : `str` \\
            The input from the user.
        
        Returns
        -------
        - response.text : `str` \\
            The response from the assistant.
        """
        if self.stream:
            respond = self.chat_session.send_message_stream(user_input)
        else:
            respond = self.chat_session.send_message(user_input)
        return respond

    def chat(self) -> list[dict]:
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
            response = self.call_llm_api(user_input)
            if self.stream:
                for chunk in response:
                    print(chunk.text, end="", flush=True)
                print()
            else:
                print(response.text)
        return self.chat_session.get_history(curated=False)


if __name__ == "__main__":
    from ..utils.argparse import arg_parser

    args = arg_parser()
    gg_api = GG_AI_Studio_API("gemini-1.5-flash", args.stream)
    pprint(gg_api.chat())
