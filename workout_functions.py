import os, csv
from colored import Fore, Back, Style

menu_list = []
we_options_list = {
    " Create Workout Entry": "create_submenu('Entry', pw_file_path)",
}

wt_options_list = {
    " View Workout Templates": "display_submenu('Templates', wt_file_path)",
    " Edit Workout Templates": "display_submenu('Templates', wt_file_path)",
    " Create New Workout Template": "create_submenu('Templates', wt_file_path)",
    " Delete a Workout Template": "delete_submenu('Templates', wt_file_path, wt_header)",
}

el_options_list = {
    " Display all exercises in database": "el_display()",
    " Edit an exercise from the database": "display_submenu('Exercises', el_file_path)",
    " Add a new exercise to the database": "create_submenu('Exercises', el_file_path)",
    " Delete an exercise from the database": "delete_submenu('Exercises', el_file_path, el_header)",
}

pw_options_list = {
    " View a Workout Log": "display_submenu('Log', pw_file_path)",
    " Delete a Workout Log": "delete_submenu('Log', pw_file_path, pw_header)",
}

pw_file_path = "previous_workouts.csv"
pw_header = "workout_date,template_used,completed_exercises\n"

el_file_path = "exercises.csv"
el_header = "exercise_name,default_weight,default_reps,default_sets\n"

wt_file_path = "workout_templates.csv"
wt_header = "template_name,exercise_list,default_weight,default_reps,default_sets\n"


def clear_console():
    if os.name == "nt":
        # For Windows
        os.system("cls")
    else:
        # For Unix systems
        os.system("clear")


def check_csv(file_path, header):
    try:
        with open(file_path, "r") as file:
            pass
        file.close()
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write(header)
        file.close()


# Check if CSV's exist, if not, create it
check_csv(pw_file_path, pw_header)
check_csv(el_file_path, el_header)
check_csv(wt_file_path, wt_header)


# Creates sub menu list with data from CSV depending on feature selected
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


# General menu function used to navigate through main menus of the application
def general_menu(menu_name, options_list):
    total_options = len(options_list) + 1
    user_selection = ""
    while user_selection != total_options:
        print(f"{Style.BOLD}{Fore.CYAN} -- {menu_name} Menu --\n")
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, option in enumerate(options_list):
            print(f"{Fore.blue}[ {index + 1} ]{option}")
        if menu_name == "Main":
            print(f"{Fore.RED}[ {total_options} ] Exit Application{Style.reset}")
        else:
            print(f"{Fore.CYAN}[ {total_options} ] Return to Main Menu{Style.reset}")
        user_selection = input(
            f"{Fore.green}\nEnter the function you would like to enter: {Style.reset}\n"
        )
        clear_console()
        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > total_options:
                raise ValueError
            if user_selection == total_options:
                break
            else:
                selected_option = list(options_list.keys())[user_selection - 1]
                eval(options_list[selected_option])
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and {total_options}:{Style.reset}\n"
            )


# Function used for features which have a display sub-menu
def display_submenu(menu_name, csv_path):
    clear_console()
    user_selection = ""
    viewing_template = False
    update_menu_list(csv_path)
    return_value = len(menu_list) + 1
    while user_selection != return_value:
        print(
            f"{Style.BOLD}{Fore.CYAN}-- Display Workout {menu_name} Menu --{Style.reset}\n"
        )
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, record in enumerate(menu_list):
            print(f"[ {index + 1} ] {record}")
        print(f"{Fore.CYAN}[ {return_value} ] Return to previous menu{Style.reset}")
        user_selection = input(
            f"{Fore.green}\nPlease enter the index of the record you would like to view: {Style.reset}\n"
        )
        clear_console()

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > return_value:
                raise ValueError
            if user_selection != return_value:
                selected_record = menu_list[user_selection - 1]
                viewing_template = True
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and {return_value}:{Style.reset}\n"
            )

        while viewing_template:
            clear_console()
            print(
                f"{Fore.BLUE}-- Currently viewing: {selected_record} Workout Routine --\n"
            )
            # If user selected Workout Templates menu, will print all templates
            if csv_path == wt_file_path:
                with open(csv_path, "r") as file:
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
                        if row[0] == selected_record:
                            print(f"{Fore.YELLOW}Template Name: {template_name}")
                            print(f"Exercise Lists: {exercise_list}")
                            print(f"Default Weight: {default_weight}")
                            print(f"Default Reps: {default_reps}")
                            print(f"Default Sets: {default_sets}{Style.RESET}")
                            print("\n")
                            break
                    else:
                        continue
            # If user selected Workout logs menu, will print all log records
            elif csv_path == pw_file_path:
                with open(csv_path, "r") as file:
                    csv_reader = csv.reader(file)
                    header = next(csv_reader)
                    for row in csv_reader:
                        (
                            workout_date,
                            template_used,
                            completed_exercises,
                        ) = row
                        if row[0] == selected_record:
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
            else:
                print("Sorry, there seems to be an error.")

            file.close()
            input("Press enter when you would like to return to the previous menu:\n")
            viewing_template = False
            clear_console()


# Function used for features which have a delete sub-menu
def delete_submenu(menu_name, csv_path, header):
    clear_console()
    update_menu_list(csv_path)
    user_selection = ""
    end_function = False
    return_value = len(menu_list) + 1
    while user_selection != return_value:
        delete_loop = False
        user_confirmation = False
        print(
            f"{Style.BOLD}{Fore.red}-- Delete Workout {menu_name} Menu --{Style.reset}\n"
        )
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, record in enumerate(menu_list):
            print(f"[ {index + 1} ] {record}")
        print(
            f"{Style.BOLD}{Fore.YELLOW}[ {return_value} ] Cancel and return to previous menu"
        )
        user_selection = input(
            f"{Fore.green}\nPlease enter the index of the record you would like to delete: {Style.reset}\n"
        )
        clear_console()

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > return_value:
                raise ValueError
            if user_selection != return_value:
                selected_record = menu_list[user_selection - 1]
                delete_loop = True
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and {return_value}:{Style.reset}\n"
            )

        while delete_loop:
            user_confirmation = input(
                f"{Style.bold}{Fore.red}Are you sure you would like to delete {selected_record}? This action cannot be undone.{Style.reset}\n{Fore.yellow}(Type 'YES' to confirm or 'NO' to abort:){Style.reset}\n"
            )
            if user_confirmation == "YES":
                clear_console()
                transfer_rows = []
                with open(csv_path, "r") as file:
                    csv_reader = csv.reader(file)
                    header = next(csv_reader, None)
                    for row in csv_reader:
                        if row[0] != selected_record:
                            transfer_rows.append(row)
                file.close()

                with open(csv_path, "w", newline="") as file:
                    # Convert header into a string instead of list
                    file.write(",".join(header) + "\n")
                    csvwriter = csv.writer(file)
                    csvwriter.writerows(transfer_rows)
                file.close()
                print(f"{Fore.red}Deleted {selected_record}{Style.reset}")
                # Update menu list so it doesn't show old records
                update_menu_list(csv_path)
                return_value = len(menu_list) + 1
                delete_loop = False
            elif user_confirmation == "NO":
                clear_console()
                print(f"{Fore.green}User cancelled. Aborting deletion..{Style.reset}")
                delete_loop = False
            else:
                clear_console()
                print("Please enter YES or NO:")


# Function for features which have an edit sub-menu
def display_submenu(menu_name, csv_path):
    pass


# Function for features which have a create sub-menu
def create_submenu(menu_name, csv_path):
    pass


# Function to display all exercises in Exercise Database
def el_display():
    clear_console()
    print(f"{Fore.blue}Displaying all exercises in Exercise Database:{Style.reset}\n")
    close_menu = False
    while not close_menu:
        with open(el_file_path, "r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            print(
                f"{Fore.CYAN}{'Exercise':<25}{'Default Weight':<15}{'Default Reps':<15}{'Default Sets':<15}{Style.RESET}"
            )
            for row in csv_reader:
                (
                    exercise_name,
                    default_weight,
                    default_reps,
                    default_sets,
                ) = row
                print(
                    f"{Fore.YELLOW}{exercise_name:<25}{default_weight:<15}{default_reps:<15}{default_sets:<15}{Style.RESET}"
                )
            print(f"\n{Fore.CYAN}[ END OF LIST ]{Style.reset}\n")
        input("Press enter when you would like to return to the exericise list menu:\n")
        close_menu = True
        clear_console()
    file.close()
    clear_console()
