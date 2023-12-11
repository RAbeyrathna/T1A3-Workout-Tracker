from colored import Fore, Back, Style
import csv

exercises_file_path = "exercises.csv"

try:
    with open(exercises_file_path, "r") as exercises_file:
        pass
    exercises_file.close()
except FileNotFoundError:
    with open(exercises_file_path, "w") as exercises_file:
        exercises_file.write("exercise_name,default_weight,default_reps,default_sets\n")
    exercises_file.close()


def el_menu():
    user_selection = ""
    while user_selection != 5:
        print(f"{Style.BOLD}{Fore.yellow} -- Exercise Database Menu --\n")
        print(f"{Fore.blue}[ 1 ] Display all exercises in database")
        print(f"[ 2 ] Edit an exercise from the database")
        print(f"[ 3 ] Add a new exercise to the database")
        print(f"[ 4 ] Delete an exercise from the database")
        print(f"[ 5 ] Return back to Main Menu{Style.reset}")
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
                f"\n{Fore.blue}Displaying all exercises in Exercise Database:{Style.reset}\n"
            )
            el_display()
        elif user_selection == 2:
            print(f"\n{Fore.blue}Choose an exercise to edit:{Style.reset}\n")
        elif user_selection == 3:
            print(f"\n{Fore.blue}Adding new exercise to the database...{Style.reset}\n")
        elif user_selection == 4:
            print(
                f"\n{Fore.blue}Choose an exercise to delete from the database:{Style.reset}\n"
            )

    print(f"{Fore.red}\nExiting Workout Templates Menu...\n{Style.reset}")


def el_display():
    with open(exercises_file_path, "r") as exercises_file:
        csv_reader = csv.reader(exercises_file)
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
    exercises_file.close()


def el_edit():
    pass


def el_add():
    pass


def el_delete():
    pass
