from colored import Fore, Back, Style
from functions import clear_console
import csv

templates_file = "workout_templates.csv"

try:
    templates_file = open(templates_file, "r")
    templates_file.close()
except FileNotFoundError:
    templates_file = open(templates_file, "w")
    templates_file.write(
        "id,template_name,exercise_list,default_weight,default_reps,default_sets\n"
    )
    templates_file.close()


def wt_menu():
    user_selection = ""
    while user_selection != 5:
        print(f"{Style.BOLD}{Fore.yellow} -- Workout Templates Menu --\n")
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        print(f"{Fore.blue}[ 1 ] View Workout Templates")
        print(f"[ 2 ] Edit Workout Templates")
        print(f"[ 3 ] Create New Workout Template")
        print(f"[ 4 ] Delete a Workout Template")
        print(f"[ 5 ] Return back to Main Menu{Style.reset}")
        user_selection = input(
            f"{Fore.green}\nEnter the function you would like to enter: {Style.reset}\n"
        )

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > 5:
                raise ValueError
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and 5:{Style.reset}\n"
            )

        if user_selection == 1:
            clear_console()
        elif user_selection == 2:
            clear_console()
        elif user_selection == 3:
            clear_console()
        elif user_selection == 4:
            clear_console()
    clear_console()


def wt_display():
    pass


def wt_edit():
    pass


def wt_create():
    pass


def wt_delete():
    pass
