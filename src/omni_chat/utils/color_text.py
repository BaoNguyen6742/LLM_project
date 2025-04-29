import colorama
from colorama import Fore

colorama.init(autoreset=True)


def color_text(text: str, color: str) -> str:
    """
    Make the text colored.
    
    Behavior
    --------
    Use colorama to color the text.
    
    Parameters
    ----------
    - text : `str` \\
        The text to be colored.
    - color : `str` \\
        The color to be used.
    
    Returns
    -------
    -  : `str`
        The colored text.
    """
    color_code = color.upper()
    colorama_color = getattr(Fore, color_code)
    return colorama_color + text
