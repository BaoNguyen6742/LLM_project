from pathlib import Path

import yaml

from omni_chat.utils.argparse import arg_parser
from omni_chat.utils.color_text import color_text
from omni_chat.utils.text_utils import clear_screen, show_models


def main():
    clear_screen()
    args = arg_parser()
    with open(Path("./src/omni_chat/model/llm_models_list.yaml"), "r") as file:
        config = yaml.safe_load(file)
    print("Select a chat client: (default is Groq, Enter for default)")
    for idx, client in enumerate(config.keys()):
        print(f"{idx + 1}. {client} ({config[client]['description']})")

    print()
    client_choice = input(
        color_text(
            "Enter your choice (default is Groq if user enter nothing): ", "green"
        )
    )
    if client_choice == "":
        client_choice = 1
    else:
        try:
            client_choice = int(client_choice)
            if client_choice < 1 or client_choice > len(config.keys()):
                raise ValueError
        except ValueError:
            print(color_text(f"{client_choice} is Invalid choice. Exiting...", "red"))
            return

    client_name = list(config.keys())[client_choice - 1]

    if client_name == "GG_AI_Studio":
        from omni_chat.API.gg_ai_studio_api import GG_AI_Studio_API as LLM_API
    elif client_name == "OpenRouter":
        from omni_chat.API.open_router_api import OpenRouter_API as LLM_API
    elif client_name == "Groq":
        from omni_chat.API.groq_api import Groq_API as LLM_API
    else:
        print(color_text(f"{client_name} is not supported. Exiting...", "red"))
        return
    model_list = list(config[client_name]["models"])
    model_selected = show_models(model_list)
    clear_screen()
    print(
        color_text(
            f'Selected model: {model_selected}, enter "<exit>" to exit the chat\n',
            "green",
        )
    )
    llm_api = LLM_API(model_selected, args.stream)
    llm_api.chat()


if __name__ == "__main__":
    main()
