import yaml
from pathlib import Path

from utils.color_text import color_text
from utils.text_utils import clear_screen, show_models


def main():
    clear_screen()
    with open(Path("./src/model/llm_models_list.yaml"), "r") as file:
        config = yaml.safe_load(file)
    print("Select a chat client: (default is Groq, Enter for default)")
    for idx, client in enumerate(config.keys()):
        print(f"{idx + 1}. {client} ({config[client]['description']})")

    print()
    client_choice = input(color_text("Enter your choice: ", "green"))
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
    print(f"Selected client: {client_name}")

    if client_name == "GG_AI_Studio":
        from API.gg_ai_studio_api import GG_AI_Studio_API

        model_list = list(config[client_name]["models"])
        model_selected = show_models(model_list)
        gg_api = GG_AI_Studio_API(model_selected)
        gg_api.call_gg_api()
    elif client_name == "OpenRouter":
        from API.open_router_api import OpenRouter_API

        open_router_api = OpenRouter_API(config[client_name]["models"])
        open_router_api.call_open_router_api()
    elif client_name == "GROQ":
        from API.groq_api import Groq_API

        groq_api = Groq_API(config[client_name]["models"])
        groq_api.call_groq_api()
    else:
        print(color_text(f"{client_name} is not supported. Exiting...", "red"))


if __name__ == "__main__":
    main()
