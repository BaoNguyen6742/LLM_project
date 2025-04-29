import math
import os
import sys

# sys.tracebacklimit = 0


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_models(model_list: list[str]) -> str:
    """
    Show the models available in the list in group of 10.
    
    Behavior
    --------
    For the list of models, show the models in group of 10., if the user presses n then move tothe next 10 models, if the user press p then move to the previous 10 models, if the user press n when there are no more model after or press p when there are no model before then don't do anything. If the user press a number that is valid for the current list of model showing then select that model and return the model name. else quit the program. 
    
    Parameters
    ----------
    - model_list : `list[str]` \\
        List of the name of all models available.
    
    Returns
    -------
    - model_name : `str` \\
        The name of the selected model.
    """
    max_split_idx = math.ceil(len(model_list) / 10) - 1
    current_split = 0
    while True:
        clear_screen()
        print("Available models:")
        begin_split = current_split * 10
        end_split = min(len(model_list), begin_split + 10)
        for i, model_name in enumerate(model_list[begin_split:end_split], start=1):
            print(f"{i}. {model_name}")
        print()
        print(
            "Press 'n' for next 10 models, 'p' for previous 10 models, or enter a number to select a model."
        )

        user_input = input("Enter your choice: ")
        if user_input == "n":
            if current_split < max_split_idx:
                current_split += 1
            else:
                continue
        elif user_input == "p":
            if current_split > 0:
                current_split -= 1
            else:
                continue
        elif user_input.isdigit():
            try:
                assert 1 <= int(user_input) <= end_split - begin_split + 1
                model_name = model_list[begin_split + int(user_input) - 1]
                return model_name
            except AssertionError:
                print(f"\nInvalid input: {user_input}. Please enter a valid number.")
                sys.exit(1)
        else:
            print("Invalid input. Please try again.")
            continue
