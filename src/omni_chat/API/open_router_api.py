from pprint import pprint

from openai import OpenAI

from ..utils.color_text import color_text
from . import api_key


class OpenRouter_API:
    def __init__(self, model_name: str = "", stream: bool = False):
        self.model_name = model_name
        self.stream = stream
        self.chat_history = []
        self.chat_session = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key.OPENROUTER_API_KEY,
        )

    def call_llm_api(self, user_input: str):
        """
        Chat with the assistant.
        
        Behavior
        --------
        Chat with the assistant using the Open Router API.
        
        Parameters
        ----------
        - user_input : `str` \\
            The input from the user.
        
        Returns
        -------
        - response : `ChatCompletion | Stream[ChatCompletionChunk]` \\
            The response from the assistant.
        """
        self.chat_history.append({"role": "user", "content": user_input})
        response = self.chat_session.chat.completions.create(
            model=self.model_name, messages=self.chat_history, stream=self.stream
        )

        return response

    def chat(self) -> list[dict]:
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
            print(color_text("(assistant) >>> ", "blue"), end="")
            response = self.call_llm_api(user_input)
            complete_response = ""
            if self.stream:
                for chunk in response:
                    print(chunk.choices[0].delta.content, end="", flush=True)
                    complete_response += chunk.choices[0].delta.content
                print()
            else:
                complete_response = response.choices[0].message.content
                print(complete_response)
            self.chat_history.append(
                {"role": "assistant", "content": complete_response}
            )
            print()
        return self.chat_history


if __name__ == "__main__":
    from ..utils.argparse import arg_parser

    args = arg_parser()
    open_router_instance = OpenRouter_API(
        model_name="google/gemma-2-9b-it:free", stream=args.stream
    )
    pprint(open_router_instance.chat())
