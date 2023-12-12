from colored import Fore, Back, Style
from functions import clear_console
import csv


file_path = "previous_workouts.csv"

menu_list = []

try:
    with open(file_path, "r") as file:
        pass
    file.close()
except FileNotFoundError:
    with open(file_path, "w") as file:
        file.write("workout_date,template_used,completed_exercises\n")
    file.close()


### Could not import as global function - Investigate later, does not append data to menu_list
def update_menu_list(file_path):
    global menu_list
    menu_list = []
    try:
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for row in csv_reader:
                menu_list.append(row[0])
    except FileNotFoundError:
        print(f"File not found: {file_path}")


update_menu_list(file_path)


def pw_menu():
    user_selection = ""
    while user_selection != 3:
        print(f"{Style.BOLD}{Fore.CYAN} -- Workout History Menu --\n")
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        print(f"{Fore.blue}[ 1 ] View a Workout Log")
        print(f"[ 2 ] Delete a Workout Log")
        print(f"[ 3 ] Return back to Main Menu{Style.reset}")
        user_selection = input(
            f"{Fore.green}\nEnter the function you would like to enter: {Style.reset}\n"
        )
        clear_console()

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > 3:
                raise ValueError
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and 3:{Style.reset}\n"
            )

        if user_selection == 1:
            clear_console()
            pw_display()
        elif user_selection == 2:
            clear_console()
            pw_delete()
    clear_console()


def pw_display():
    pass


def pw_delete():
    pass
