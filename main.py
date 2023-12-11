from colored import Fore, Back, Style
from workout_templates import wt_menu
from workout_entry import we_menu
from exercise_list import el_menu
from previous_workouts import pw_menu

print(
    f"{Style.BOLD}{Fore.YELLOW}\nWelcome the the Workout Tracker application. Please select from the following options:{Style.reset}\n"
)


def display_menu():
    user_selection = ""
    while user_selection != 5:
        print(f"{Style.BOLD}{Fore.yellow} -- Main Menu --\n")
        print(f"{Fore.cyan}[ 1 ] Enter Workout Entry")
        print(f"[ 2 ] Enter Workout Templates Menu")
        print(f"[ 3 ] View Exercise List Database")
        print(f"[ 4 ] View Previous Workout Entries")
        print(f"[ 5 ] Exit the Program{Style.reset}")
        user_selection = input(
            f"{Fore.green}\nEnter the function you would like to enter: {Style.reset}\n"
        )

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > 5:
                raise ValueError
        except ValueError:
            print(
                f"\n{Fore.red}Please enter a valid number between 1 and 5:{Style.reset}\n"
            )

        if user_selection == 1:
            print(
                f"\n{Fore.blue}Entering 'Enter Workout Entry' Function...{Style.reset}\n"
            )
            we_menu()
        elif user_selection == 2:
            print(f"\n{Fore.blue}Entering 'Workout Templates' Menu...{Style.reset}\n")
            wt_menu()
        elif user_selection == 3:
            print(
                f"\n{Fore.blue}Entering 'View Exercise List Database' Function...{Style.reset}\n"
            )
            el_menu()
        elif user_selection == 4:
            print(
                f"\n{Fore.blue}Entering 'View Previous Workout Entries' Function...{Style.reset}\n"
            )
            pw_menu()
    print(f"{Fore.red}\nQuitting the application...{Style.reset}\n")


display_menu()
