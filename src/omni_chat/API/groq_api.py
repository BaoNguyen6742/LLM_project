from pprint import pprint

from groq import Groq

from omni_chat.utils.color_text import color_text

from . import api_key


class Groq_API:
    def __init__(self, model_name: str = "", stream: bool = False):
        self.chat_history = []
        self.model_name = model_name
        self.stream = stream
        self.client = Groq(api_key=api_key.GROQ_API_KEY)

    def call_llm_api(self, user_input: str):
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
        return response

    def chat(self):
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
            print(color_text("(assistant) >>> ", "blue"), end="")
            response = self.call_llm_api(user_input)
            complete_response = ""
            if self.stream:
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        print(chunk.choices[0].delta.content, end="", flush=True)
                        complete_response += chunk.choices[0].delta.content
                print()
            else:
                complete_response = response.choices[0].message.content
                print(complete_response)
            self.chat_history.append(
                {"role": "assistant", "content": complete_response}
            )
        return self.chat_history


if __name__ == "__main__":
    from omni_chat.utils.argparse import arg_parser

    args = arg_parser()
    open_router_instance = Groq_API(model_name="gemma2-9b-it", stream=args.stream)
    pprint(open_router_instance.chat())
