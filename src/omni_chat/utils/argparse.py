import argparse


def arg_parser():
    """
    Parse the command line arguments.
    
    Behavior
    --------
    Parse the command line arguments and return the parsed arguments.
    
    Returns
    -------
    - args : `argparse.Namespace` \\
        The parsed arguments.
    """

    parser = argparse.ArgumentParser(description="Chat with LLMs")
    parser.add_argument(
        "-s", "--stream", action="store_true", help="Enable streaming mode"
    )
    return parser.parse_args()
