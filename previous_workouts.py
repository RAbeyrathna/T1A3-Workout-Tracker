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
    clear_console()
    user_selection = ""
    viewing_template = False
    return_value = len(menu_list) + 1
    while user_selection != return_value:
        print(f"{Style.BOLD}{Fore.CYAN}-- Display Workout Logs --{Style.reset}\n")
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, log in enumerate(menu_list):
            print(f"[ {index + 1} ] {log}")
        print(f"[ {return_value} ] Return to Workout History Menu")
        user_selection = input(
            f"{Fore.green}\nPlease enter the index of the log you would like to view: {Style.reset}\n"
        )
        clear_console()

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > return_value:
                raise ValueError
            if user_selection != return_value:
                selected_log = menu_list[user_selection - 1]
                viewing_template = True
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and {return_value}:{Style.reset}\n"
            )

        while viewing_template:
            clear_console()
            print(f"{Fore.BLUE}-- Currently viewing: {selected_log} Workout Log --\n")
            with open(file_path, "r") as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)
                for row in csv_reader:
                    (
                        workout_date,
                        template_used,
                        completed_exercises,
                    ) = row
                    if row[0] == selected_log:
                        print(f"{Fore.GREEN}Workout Date: {workout_date}")
                        print(f"Template Used: {template_used}{Style.reset} \n")
                        # Convert string into proper dictionary
                        exercises_dict = eval(completed_exercises)
                        print(
                            f"{Fore.CYAN}{'Exercise':<25}{'Working Weight (kg)':<20}{'Working Reps':<15}{'Working Sets':<15}{Style.RESET}"
                        )
                        for exercise, info in exercises_dict.items():
                            working_weight, working_reps, working_sets = info
                            print(
                                f"{Fore.YELLOW}{exercise:<25}{working_weight:<20}{working_reps:<15}{working_sets:<15}{Style.RESET}"
                            )
                        print("\n")
                        break
                    else:
                        continue
            file.close()
            input("Press enter when you would like to return to the previous menu:\n")
            viewing_template = False
            clear_console()


def pw_delete():
    pass
