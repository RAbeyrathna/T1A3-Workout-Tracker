import os, csv
from colored import Fore, Back, Style

we_options_list = {
    " Create Workout Entry": "wt_display()",
}

wt_options_list = {
    " View Workout Templates": "wt_display()",
    " Edit Workout Templates": "wt_edit()",
    " Create New Workout Template": "wt_create()",
    " Delete a Workout Template": "wt_delete()",
}

el_options_list = {
    " Display all exercises in database": "el_display()",
    " Edit an exercise from the database": "el_edit()",
    " Add a new exercise to the database": "el_add()",
    " Delete an exercise from the database": "el_delete()",
}

pw_options_list = {
    " View a Workout Log": "pw_display()",
    " Delete a Workout Log": "pw_delete()",
}


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
