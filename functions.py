import os


def clear_console():
    if os.name == "nt":
        # For Windows
        os.system("cls")
    else:
        # For Unix systems
        os.system("clear")
