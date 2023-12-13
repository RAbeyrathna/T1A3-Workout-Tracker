import os, csv
from colored import Fore, Back, Style

menu_list = []

wt_options_list = {
    " Create a New Workout Template": "create_submenu('Templates', wt_file_path)",
    " View all Workout Templates": "display_records('Templates', wt_file_path)",
    " Edit Workout Templates": "edit_submenu('Templates', wt_file_path)",
    " Delete a Workout Template": "delete_submenu('Templates', wt_file_path, wt_header)",
}

el_options_list = {
    " Create a new exercise": "create_submenu('Exercises', el_file_path)",
    " View all Exercises": "el_display()",
    " Edit an Exercise": "edit_submenu('Exercises', el_file_path)",
    " Delete an Exercise": "delete_submenu('Exercises', el_file_path, el_header)",
}

pw_options_list = {
    " Create a new Workout Entry": "create_submenu('Entry', pw_file_path)",
    " View all Workout Logs": "display_records('Log', pw_file_path)",
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
            print(f"{Fore.YELLOW}[ {total_options} ] Return to Main Menu{Style.reset}")
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


# Function used to display menu_list items as menu options
def display_menu_list(menu_name, return_value):
    user_selection = ""
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
                return user_selection
            elif user_selection == return_value:
                return user_selection
        except ValueError:
            clear_console()
            print(
                f"{Fore.red}Please enter a valid number between 1 and {return_value}:{Style.reset}\n"
            )


# Function used to display records for features
def display_records(menu_name, csv_path):
    clear_console()
    update_menu_list(csv_path)
    return_value = len(menu_list) + 1
    user_selection = display_menu_list(menu_name, return_value)

    if csv_path == wt_file_path:
        with open(csv_path, "r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            selected_record = menu_list[user_selection - 1]
            for row in csv_reader:
                template_name, exercise_list = row
                if row[0] == selected_record:
                    exercises_dict = eval(exercise_list)
                    print(
                        f"{Fore.BLUE}-- Viewing Workout Template: {template_name} --{Style.reset}\n"
                    )
                    print(
                        f"{Fore.CYAN}{'Exercise':<25}{'Default Weight (kg)':<20}{'Default Reps':<15}{'Default Sets':<15}{Style.RESET}"
                    )
                    for exercise, info in exercises_dict.items():
                        default_weight, default_reps, default_sets = info
                        print(
                            f"{Fore.YELLOW}{exercise:<25}{default_weight:<20}{default_reps:<15}{default_sets:<15}{Style.RESET}"
                        )
                    print("\n")
                    input(
                        "Press enter when you would like to return to the previous menu:\n"
                    )
                    clear_console()
                    break
            else:
                print("Sorry, there seems to be an error.")
        file.close()
        clear_console()
    elif csv_path == pw_file_path:
        with open(csv_path, "r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            selected_record = menu_list[user_selection - 1]
            for row in csv_reader:
                (
                    workout_date,
                    template_used,
                    completed_exercises,
                ) = row
                if row[0] == selected_record:
                    print(
                        f"{Fore.BLUE}-- Viewing Workout Log: {workout_date} --{Style.reset}\n"
                    )
                    print(f"{Fore.GREEN}Template Used: {template_used}{Style.reset} \n")
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
                    input(
                        "Press enter when you would like to return to the previous menu:\n"
                    )
                    clear_console()
                    break
                else:
                    continue
        file.close()
        clear_console()


# Function used for features which have a delete sub-menu
def delete_submenu(menu_name, csv_path, header):
    clear_console()
    delete_loop = False
    update_menu_list(csv_path)
    return_value = len(menu_list) + 1
    user_selection = display_menu_list(menu_name, return_value)
    if user_selection != return_value:
        selected_record = menu_list[user_selection - 1]
        delete_loop = True
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


# Function for features which have a create sub-menu
def create_submenu(menu_name, csv_path):
    pass


# Function for features which have an edit sub-menu
def edit_submenu(menu_name, csv_path):
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
