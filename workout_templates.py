from colored import Fore, Back, Style
from functions import clear_console
import csv

file_path = "workout_templates.csv"

menu_list = []

try:
    with open(file_path, "r") as file:
        pass
    file.close()
except FileNotFoundError:
    with open(file_path, "w") as file:
        file.write(
            "template_name,exercise_list,default_weight,default_reps,default_sets\n"
        )
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
    return_value = len(menu_list) + 1
    while user_selection != return_value:
        print(f"{Style.BOLD}{Fore.CYAN}-- Display Workout Templates --{Style.reset}\n")
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, template in enumerate(menu_list):
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
                selected_routine = menu_list[user_selection - 1]
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
            with open(file_path, "r") as file:
                csv_reader = csv.reader(file)
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
                        print(f"Exercise Lists: {exercise_list}")
                        print(f"Default Weight: {default_weight}")
                        print(f"Default Reps: {default_reps}")
                        print(f"Default Sets: {default_sets}{Style.RESET}")
                        print("\n")
                        break
                    else:
                        continue
            file.close()
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
    end_function = False
    return_value = len(menu_list) + 1
    while user_selection != return_value:
        delete_loop = False
        user_confirmation = False
        print(f"{Style.BOLD}{Fore.red}-- Delete Workout Templates --{Style.reset}\n")
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, template in enumerate(menu_list):
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
                selected_routine = menu_list[user_selection - 1]
                delete_loop = True
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and {return_value}:{Style.reset}\n"
            )

        while delete_loop:
            user_confirmation = input(
                f"{Style.bold}{Fore.red}Are you sure you would like to delete {selected_routine}? This action cannot be undone.{Style.reset}\n{Fore.yellow}(Type 'YES' to confirm or 'NO' to abort:){Style.reset}\n"
            )
            if user_confirmation == "YES":
                clear_console()
                transfer_rows = []
                with open(file_path, "r") as file:
                    csv_reader = csv.reader(file)
                    header = next(csv_reader, None)
                    for row in csv_reader:
                        if row[0] != selected_routine:
                            transfer_rows.append(row)
                file.close()

                with open(file_path, "w", newline="") as file:
                    file.write(
                        "template_name,exercise_list,default_weight,default_reps,default_sets\n"
                    )
                    csvwriter = csv.writer(file)
                    csvwriter.writerows(transfer_rows)
                file.close()
                print(f"{Fore.red}Deleted {selected_routine}{Style.reset}")
                update_menu_list(file_path)
                return_value = len(menu_list) + 1
                delete_loop = False
            elif user_confirmation == "NO":
                clear_console()
                print(f"{Fore.green}User cancelled. Aborting deletion..{Style.reset}")
                delete_loop = False
            else:
                clear_console()
                print("Please enter YES or NO:")
