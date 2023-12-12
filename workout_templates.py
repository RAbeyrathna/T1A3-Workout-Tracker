from colored import Fore, Back, Style
from functions import clear_console
import csv

templates_file_path = "workout_templates.csv"

try:
    with open(templates_file_path, "r") as templates_file:
        pass
    templates_file.close()
except FileNotFoundError:
    with open(exercises_file_path, "w") as exercises_file:
        templates_file.write(
            "template_name,exercise_list,default_weight,default_reps,default_sets\n"
        )
    templates_file.close()

template_list = []

# Need to do error checking and testing for the below
with open(templates_file_path, "r") as templates_file:
    csv_reader = csv.reader(templates_file)
    header = next(csv_reader)
    for row in csv_reader:
        template_list.append(row[0])


def wt_menu():
    user_selection = ""
    while user_selection != 5:
        print(f"{Style.BOLD}{Fore.CYAN} -- Workout Templates Menu --\n")
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
        clear_console()

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
            wt_display()
        elif user_selection == 2:
            clear_console()
        elif user_selection == 3:
            clear_console()
        elif user_selection == 4:
            clear_console()
            wt_delete()
    clear_console()


def wt_display():
    clear_console()
    user_selection = ""
    viewing_template = False
    return_value = len(template_list) + 1
    while user_selection != return_value:
        print(f"{Style.BOLD}{Fore.CYAN}-- Display Workout Templates --{Style.reset}\n")
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, template in enumerate(template_list):
            print(f"[ {index + 1} ] {template}")
        print(f"[ {return_value} ] Return to Workout Templates Menu")
        user_selection = input(
            f"{Fore.green}\nPlease enter the index of the template you would like to view: {Style.reset}\n"
        )
        clear_console()

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > return_value:
                raise ValueError
            if user_selection != return_value:
                selected_routine = template_list[user_selection - 1]
                viewing_template = True
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and {return_value}:{Style.reset}\n"
            )

        while viewing_template:
            clear_console()
            print(
                f"{Fore.BLUE}-- Currently viewing: {selected_routine} Workout Routine --\n"
            )
            with open(templates_file_path, "r") as templates_file:
                csv_reader = csv.reader(templates_file)
                header = next(csv_reader)
                for row in csv_reader:
                    (
                        template_name,
                        exercise_list,
                        default_weight,
                        default_reps,
                        default_sets,
                    ) = row
                    if row[0] == selected_routine:
                        print(f"{Fore.YELLOW}Template Name: {template_name}")
                        print(f"Exercise Lists: {exercise_list:<15}")
                        print(f"Default Weight: {default_weight:<15}")
                        print(f"Default Reps: {default_reps:<15}")
                        print(f"Default Sets: {default_sets:<15}{Style.RESET}")
                        print("\n")
                        break
                    else:
                        continue
            templates_file.close()
            input("Press enter when you would like to return to the previous menu:\n")
            viewing_template = False
            clear_console()


def wt_edit():
    pass


def wt_create():
    pass


def wt_delete():
    clear_console()
    user_selection = ""
    return_value = len(template_list) + 1
    while user_selection != return_value:
        delete_loop = False
        user_confirmation = False
        print(f"{Style.BOLD}{Fore.red}-- Delete Workout Templates --{Style.reset}\n")
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, template in enumerate(template_list):
            print(f"[ {index + 1} ] {template}")
        print(f"[ {return_value} ] Return to Workout Templates Menu")
        user_selection = input(
            f"{Fore.green}\nPlease enter the index of the template you would like to delete: {Style.reset}\n"
        )
        clear_console()

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > return_value:
                raise ValueError
            if user_selection != return_value:
                selected_routine = template_list[user_selection - 1]
                delete_loop = True
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and {return_value}:{Style.reset}\n"
            )

        while delete_loop:
            user_confirmation = input(
                f"{Style.bold}{Fore.red}Are you sure you would like to delete {selected_routine}? (Type 'YES' to confirm or 'NO' to abort:){Style.reset}\n"
            )
            if user_confirmation == "YES":
                clear_console()
                print(f"{Fore.red}Deleting {selected_routine}{Style.reset}")
                delete_loop = False
            elif user_confirmation == "NO":
                clear_console()
                print(f"{Fore.green}User cancelled. Aborting deletion..{Style.reset}")
                delete_loop = False
            else:
                clear_console()
                print("Please enter YES or NO:")
