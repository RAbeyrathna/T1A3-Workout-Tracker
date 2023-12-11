from colored import Fore, Back, Style

print(
    f"{Style.BOLD}{Fore.YELLOW}\nWelcome the the Workout Tracker application. Please select from the following options:{Style.reset}\n"
)


def display_menu():
    user_selection = ""
    while user_selection != 7:
        print(f"{Fore.white}[ 1 ] Enter Workout Entry")
        print(f"[ 2 ] Create Custom Workout Template")
        print(f"[ 3 ] View Existing Workout Templates")
        print(f"[ 4 ] Edit Existing Workout Templates")
        print(f"[ 5 ] View Exercise List Database")
        print(f"[ 6 ] View Previous Workout Entries")
        print(f"[ 7 ] Exit the Program{Style.reset}")
        user_selection = input(
            f"{Fore.green}\nEnter the function you would like to enter: {Style.reset}\n"
        )

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > 7:
                raise ValueError
        except ValueError:
            print(
                f"\n{Fore.red}{Back.white}Please enter a valid number between 1 and 7:{Style.reset}\n"
            )

        if user_selection == 1:
            print("\nEntering 'Enter Workout Entry' Function...\n")
        elif user_selection == 2:
            print("\nEntering 'Create Custom Workout Template' Function...\n")
        elif user_selection == 3:
            print("\nEntering 'View Existing Workout Templates'...\n")
        elif user_selection == 4:
            print("\nEntering 'Edit Existing Workout Templates' Function...\n")
        elif user_selection == 5:
            print("\nEntering 'View Exercise List Database' Function...\n")
        elif user_selection == 6:
            print("\nEntering 'View Previous Workout Entries' Function...\n")
    print("Quitting the application...")


display_menu()
