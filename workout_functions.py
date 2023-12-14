import os, csv
from colored import Fore, Back, Style
from prettytable import PrettyTable
from datetime import datetime

# Variables

pw_file_path = "previous_workouts.csv"
pw_header = "workout_date,template_used,completed_exercises\n"

el_file_path = "exercises.csv"
el_header = "exercise_name,default_weight,default_reps,default_sets\n"

wt_file_path = "workout_templates.csv"
wt_header = "template_name,exercises\n"

menu_list = []

# Menu Option Variables to access features

# Main Menu Options
main_options_list = {
    " Enter Workout Entry Menu": "general_menu('Workout Entry', pw_options_list)",
    " Enter Workout Templates Menu": "general_menu('Workout Templates', wt_options_list)",
    " View Exercise List Database": "general_menu('Exercise Database', el_options_list)",
}

# Workout Template Options
wt_options_list = {
    " Create a New Workout Template": "create_submenu('template', wt_file_path)",
    " View all Workout Templates": "display_records('Templates', wt_file_path, 'Display')",
    " Delete a Workout Template": "delete_submenu('Templates', wt_file_path, wt_header)",
}

# Exercise List Options
el_options_list = {
    " Create a new exercise": "create_submenu('exercise', el_file_path)",
    " View all Exercises": "el_display(el_file_path)",
    " Delete an Exercise": "delete_submenu('Exercises', el_file_path, el_header)",
}

# Workout Entry/Previous Workout Options
pw_options_list = {
    " Create a new Workout Entry": "create_workout_entry('Entry', wt_file_path, pw_file_path)",
    " View all Workout Logs": "display_records('Entry', pw_file_path, 'Display')",
    " Delete a Workout Log": "delete_submenu('Log', pw_file_path, pw_header)",
}


# Function to clear the console
def clear_console():
    if os.name == "nt":
        # For Windows
        os.system("cls")
    else:
        # For Unix systems
        os.system("clear")


# Function to check if CSV file exists
def check_csv(file_path, header):
    try:
        with open(file_path, "r") as file:
            pass
        file.close()
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write(header)
        file.close()


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
                f"{Fore.red}Error: Please enter a valid number between 1 and {total_options}:{Style.reset}\n"
            )


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


# Function used to display menu_list items as menu options
def display_menu_list(menu_name, return_value, function):
    user_selection = ""
    while user_selection != return_value:
        print(
            f"{Style.BOLD}{Fore.CYAN}-- {function} Workout {menu_name} Menu --{Style.reset}\n"
        )
        print(
            f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
        )
        for index, record in enumerate(menu_list):
            print(f"[ {index + 1} ] {record}")
        print(f"{Fore.YELLOW}[ {return_value} ] Return to previous menu{Style.reset}")
        if menu_name == "Entry":
            user_selection = input(
                f"{Fore.green}\nPlease enter the index of the template you would like to use: {Style.reset}\n"
            )
        else:
            user_selection = input(
                f"{Fore.green}\nPlease enter the index of the record you would like to {function.lower()}: {Style.reset}\n"
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
                f"{Fore.red}Error: Please enter a valid number between 1 and {return_value}:{Style.reset}\n"
            )


# Function used to print records for features
def display_records(menu_name, csv_path, function):
    clear_console()
    update_menu_list(csv_path)
    return_value = len(menu_list) + 1
    user_selection = display_menu_list(menu_name, return_value, function)
    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        if user_selection != return_value:
            selected_record = menu_list[user_selection - 1]
            # If Workout Templates CSV was loaded
            if csv_path == wt_file_path and menu_name == "Templates":
                wt_display(csv_reader, selected_record)
            elif csv_path == wt_file_path and menu_name == "Entry":
                file.close()
                return selected_record
            # If Previous Workouts CSV was loaded
            elif csv_path == pw_file_path:
                pw_display(csv_reader, selected_record)
    file.close()
    clear_console()


# Function to display Previous Workout Logs
def pw_display(csv_reader, selected_record):
    for row in csv_reader:
        (workout_date, template_used, completed_exercises) = row
        if row[0] == selected_record:
            print(
                f"{Fore.BLUE}-- Viewing Workout Log: {workout_date} --{Style.reset}\n"
            )
            print(f"{Fore.GREEN}Template Used: {template_used}{Style.reset} \n")
            # Convert string into proper dictionary
            exercises_dict = eval(completed_exercises)
            workout_entry_table = PrettyTable()
            workout_entry_table.field_names = ["Exercise", "Recorded Weight (kg)"]
            for exercise, weight in exercises_dict.items():
                workout_entry_table.add_row([exercise, weight])
            print(workout_entry_table)
            print("\n")
            input(
                f"{Fore.GREEN}Press enter when you would like to return to the previous menu:{Style.RESET}\n"
            )
            clear_console()
            break


# Function to display Workout Templates
def wt_display(csv_reader, selected_record):
    for row in csv_reader:
        template_name, exercise_list = row
        if row[0] == selected_record:
            exercises_dict = eval(exercise_list)
            print(
                f"{Fore.BLUE}-- Viewing Workout Template: {template_name} --{Style.reset}\n"
            )
            template_table = PrettyTable()
            template_table.field_names = ["Exercise", "Last Working Weight (kg)"]
            for exercise, weight in exercises_dict.items():
                template_table.add_row([exercise, weight])
            print(template_table)
            print("\n")
            input(
                f"{Fore.GREEN}Press enter when you would like to return to the previous menu:\n"
            )
            clear_console()
            break


# Function to display all exercises in Exercise Database
def el_display(csv_path):
    clear_console()
    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        print(
            f"{Fore.blue}Displaying all exercises in Exercise Database:{Style.reset}\n"
        )
        exercise_table = PrettyTable()
        exercise_table.field_names = ["Exercise", "PB Weight (kg)"]

        for row in csv_reader:
            (
                exercise_name,
                pb_weight,
            ) = row
            exercise_table.add_row(row)
        print(exercise_table)
        print(f"\n{Fore.CYAN}[ END OF LIST ]{Style.reset}\n")
        input("Press enter when you would like to return to the exericise list menu:\n")
        clear_console()
    file.close()


# Function to get name for new record to be created (Exercise and Template features)
def get_record_name(record_type):
    valid_name = False
    if record_type == "template exercise":
        print(
            f"{Fore.CYAN}Please enter the name of the exercise you would like to add:{Style.reset}"
        )
        record_name = input(
            f"{Fore.YELLOW}Type 'done' when you've added all of your exercises: {Style.reset}\n"
        )
        clear_console()
    else:
        record_name = input(
            f"{Fore.BLUE}Please enter the name of the {record_type} you are creating:{Style.reset}\n"
        )
        clear_console()
    while not valid_name:
        if record_name.isdigit():
            record_name = input(
                f"{Fore.RED}Error: {record_type.capitalize()} name cannot be a number. Please try again:{Style.reset}\n"
            )
        elif len(record_name) < 3:
            record_name = input(
                f"{Fore.RED}Error: {record_type.capitalize()} name must be at least 3 characters. Please try again:{Style.reset}\n"
            )
        elif len(record_name) > 20:
            record_name = input(
                f"{Fore.RED}Error: {record_type.capitalize()} name cannot exceed 20 characters. Please try again:{Style.reset}\n"
            )
        else:
            valid_name = True
            record_name = record_name.title()
    return record_name


# Function to check if record already exists in CSV
def check_record_exists(file_path, record_name):
    record_exists = False
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)
        for row in csv_reader:
            if row[0].lower() == record_name.lower():
                record_exists = True
            else:
                continue
    file.close()
    return record_exists


# Function to prompt user to type exercise PB
def get_current_pb():
    valid_name = False
    current_pb = input(
        f"{Fore.CYAN}Please enter your current PB for this exercise (in kg):{Style.reset}\n"
    )
    while not valid_name:
        if not current_pb.isdigit():
            current_pb = input(f"{Fore.RED}PB must be a digit:{Style.reset}\n")
        elif len(current_pb) > 4:
            current_pb = input(f"{Fore.RED}PB cannot exceed 4 digits:{Style.reset}\n")
        else:
            valid_name = True
    return current_pb


# Function to create append_data variable to add to CSV
def get_append_data(record_name, file_path):
    if file_path == el_file_path:
        current_pb = get_current_pb()
        clear_console()
        append_data = [record_name, current_pb]
    elif file_path == wt_file_path:
        exercise_list = {}
        user_input = ""
        exercise_key = ""
        while exercise_key.lower() != "done":
            print(f"-- Template Name: {record_name} --\n")
            exercise_key = get_record_name("template exercise")
            if exercise_key.lower() == "done":
                break
            else:
                exercise_key = exercise_key.title()

            exercise_exists = check_record_exists(el_file_path, exercise_key)
            if exercise_exists:
                exercise_list[exercise_key] = 0
                print(f"{Fore.GREEN}Added {exercise_key}{Style.reset}")
            else:
                print(
                    f"{Fore.RED}Error: {Fore.YELLOW}{exercise_key}{Style.reset}{Fore.RED} does not exist in database. Did you want to add it?{Style.reset}\n"
                )
                add_exercise_loop = True
                add_exercise = input(f"{Fore.YELLOW}Type 'YES' or 'NO':{Style.reset}\n")
                while add_exercise_loop:
                    if add_exercise == "YES":
                        current_pb = get_current_pb()
                        append_exercise_data = [exercise_key, current_pb]
                        exercise_empty = check_record_empty(
                            el_file_path, append_exercise_data
                        )
                        if not exercise_empty:
                            append_csv(el_file_path, append_exercise_data, "exercise")
                            exercise_list[exercise_key] = 0
                            add_exercise_loop = False
                        else:
                            print(
                                f"{Fore.RED}Sorry, there was an error adding that exercise.{Style.reset}"
                            )
                            break
                    elif add_exercise == "NO":
                        add_exercise_loop = False
                        clear_console()
                        continue
                    else:
                        add_exercise = input(
                            f"{Fore.RED}Error: Please type 'YES' or 'NO':{Style.reset}\n"
                        )
        append_data = {record_name: exercise_list}
    clear_console()
    return append_data


# Function to confirm if record should be saved to CSV
def confirm_record(file_path, record_name, append_data):
    clear_console()
    user_input = ""
    if file_path == el_file_path:
        print(
            f"{Fore.blue}Would you like to save the following exercise?{Style.RESET}\n"
        )
        exercise_table = PrettyTable()
        exercise_table.field_names = ["Exercise", "PB Weight (kg)"]
        exercise_table.add_row(append_data)
        print(exercise_table)
    elif file_path == wt_file_path:
        print(
            f"{Fore.BLUE}Would you like to save the following template?{Style.RESET}\n"
        )
        print(f"{Fore.YELLOW}Template Name: {record_name}{Style.reset}\n")
        template_table = PrettyTable()
        template_table.field_names = ["Exercise", "Last Working Weight (kg)"]
        for routine, exercises in append_data.items():
            for exercise, weight in exercises.items():
                template_table.add_row([exercise, weight])
        print(template_table)
    create_record = create_record_loop()
    return create_record


def create_record_loop():
    create_record = False
    while create_record == False:
        user_input = input(f"{Fore.GREEN}\nPlease enter 'YES' or 'NO':{Style.RESET}\n")
        if user_input == "YES":
            clear_console()
            create_record = True
            return create_record
        elif user_input == "NO":
            create_record = False
            clear_console()
            return create_record
        else:
            print(f"{Fore.RED}Invalid input. Please enter 'YES' or 'NO':{Style.RESET}")


# Function to create and add function to specified CSV
def append_csv(file_path, append_data, record_type):
    with open(file_path, "a", newline="") as file:
        csv_writer = csv.writer(file)
        if file_path == wt_file_path:
            template_name = list(append_data.keys())[0]
            exercise_dict = append_data[template_name]
            csv_writer.writerow([template_name, exercise_dict])
        else:
            csv_writer.writerow(append_data)
    file.close()
    clear_console()
    print(f"{Fore.GREEN}Success! Added {record_type} to database!\n{Style.RESET}")


# Exercise List Function to add exercise to the CSV
def create_submenu(record_type, file_path):
    clear_console()
    record_name = get_record_name(record_type)
    record_exists = check_record_exists(file_path, record_name)
    while record_exists:
        print(
            f"{Fore.RED}Oops, looks like that {record_type} already exists.{Style.RESET}\n"
        )
        record_name = get_record_name(record_type)
        record_exists = check_record_exists(file_path, record_name)
    append_data = get_append_data(record_name, file_path)
    record_empty = check_record_empty(file_path, append_data)
    if not record_empty:
        create_record = confirm_record(file_path, record_name, append_data)
        if create_record:
            append_csv(file_path, append_data, record_type)
        else:
            print(f"{Fore.GREEN}Aborting function...{Style.RESET}")
    else:
        print(
            f"{Fore.RED}That {record_type} is empty. Aborting creation..{Style.RESET}\n"
        )


# Checks if the record holds any data to be appended
def check_record_empty(file_path, append_data):
    is_empty = True
    # Checks at least 1 exercise has been added to Workout Templates
    if file_path == wt_file_path:
        template_name = list(append_data.keys())[0]
        is_empty = not (bool(append_data[template_name]))
    # Checks PB Entry exists and is an integer for Exercises
    elif file_path == el_file_path:
        try:
            float(append_data[1])
            is_empty = False
        except (ValueError, TypeError):
            print(f"{Fore.RED}Error: PB Entry is not an integer{Style.reset}")
        except IndexError:
            print(f"{Fore.RED}Error: PB entry does not exist{Style.reset}")
    return is_empty


# Updates Workout Template with last workout weight values
def upd_template_weight(selected_template, exercise_data, template_path):
    updated_template = [selected_template, exercise_data]
    transfer_rows = []
    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)
        for row in csv_reader:
            if row[0] != selected_template:
                transfer_rows.append(row)
    file.close()


# Function to delete row from CSV
def delete_csv_row(csv_path, selected_record):
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


# Function to create a workout entry
def create_workout_entry(menu_name, template_path, result_path):
    workout_date = datetime.today().strftime("%Y-%m-%d")
    selected_template = display_records("Entry", template_path, "Create")
    exercise_data = get_exercise_data(template_path, selected_template)
    workout_entry = [workout_date, selected_template, exercise_data]
    create_entry = confirm_workout_entry(workout_date, selected_template, exercise_data)
    if create_entry:
        append_csv(result_path, workout_entry, "Workout Entry")
        upd_template_weight(selected_template, exercise_data, template_path)
    else:
        print(f"{Fore.RED}Aborting Workout Entry..{Style.reset}")


# Function to display workout and and confirm if it should be saved
def confirm_workout_entry(workout_date, selected_template, exercise_data):
    print(
        f"{Fore.BLUE}Would you like to save the following Workout Entry?{Style.RESET}\n"
    )
    print(f"{Fore.YELLOW}Entry Date: {workout_date}{Style.reset}\n")
    print(f"{Fore.YELLOW}Template Used: {selected_template}{Style.reset}\n")
    workout_table = PrettyTable()
    workout_table.field_names = ["Exercise", "Working Weight (kg)"]
    for exercise, weight in exercise_data.items():
        workout_table.add_row([exercise, weight])
    print(workout_table)
    create_record = create_record_loop()
    return create_record


# Function for create_workout_entry to loop through exercises in selected template
def get_exercise_data(template_path, selected_template):
    exercise_entries = {}
    with open(template_path, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            template_name, exercise_list = row
            if row[0] == selected_template:
                exercises_dict = eval(exercise_list)
                for exercise_key in exercises_dict:
                    # ADD DATA TYPE CHECKING HERE
                    print(f"-- Enter Working Weight for {exercise_key} --")
                    working_weight = input(
                        f"What was your working weight for this exercise?"
                    )
                    working_weight = int(working_weight)
                    # ADD FUNCTION TO CHECK IF WORKING WEIGHT IS NEW PB
                    exercise_entries[exercise_key] = working_weight
    file.close()
    return exercise_entries


# Function used for features which have a delete sub-menu
def delete_submenu(menu_name, csv_path, header):
    clear_console()
    delete_loop = False
    update_menu_list(csv_path)
    return_value = len(menu_list) + 1
    user_selection = display_menu_list(menu_name, return_value, "Delete")
    if user_selection != return_value:
        selected_record = menu_list[user_selection - 1]
        delete_loop = True
    while delete_loop:
        user_confirmation = input(
            f"{Style.bold}{Fore.red}Are you sure you would like to delete {selected_record}? This action cannot be undone.{Style.reset}\n{Fore.yellow}(Type 'YES' to confirm or 'NO' to abort:){Style.reset}\n"
        )
        if user_confirmation == "YES":
            clear_console()
            delete_csv_row(csv_path, selected_record)
            print(f"{Fore.red}Deleted {selected_record}{Style.reset}")
            update_menu_list(csv_path)
            return_value = len(menu_list) + 1
            delete_loop = False
        elif user_confirmation == "NO":
            clear_console()
            print(f"{Fore.green}User cancelled. Aborting deletion..{Style.reset}")
            delete_loop = False
        else:
            clear_console()
            print(f"{Fore.RED}Error: Please enter 'YES' or 'NO':{Style.reset}")
