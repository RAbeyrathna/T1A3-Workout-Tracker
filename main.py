from workout_functions import clear_console, general_menu
from colored import Fore, Back, Style

clear_console()

print(
    f"{Style.BOLD}{Fore.BLUE}Welcome the the Workout Tracker application!{Style.reset}\n"
)

main_options_list = {
    " Enter Workout Entry Menu": "general_menu('Workout Entry', pw_options_list)",
    " Enter Workout Templates Menu": "general_menu('Workout Templates', wt_options_list)",
    " View Exercise List Database": "general_menu('Exercise Database', el_options_list)",
}


general_menu("Main", main_options_list)

# def display_menu():
#     user_selection = ""
#     while user_selection != 5:
#         print(f"{Style.BOLD}{Fore.CYAN} -- Main Menu --\n")
#         print(
#             f"{Style.BOLD}{Fore.YELLOW}Please select from the following options:{Style.reset}\n"
#         )
#         print(f"{Fore.cyan}[ 1 ] Enter Workout Entry")
#         print(f"[ 2 ] Enter Workout Templates Menu")
#         print(f"[ 3 ] View Exercise List Database")
#         print(f"[ 4 ] View Previous Workout Entries")
#         print(f"[ 5 ] Exit the Program{Style.reset}")
#         user_selection = input(
#             f"{Fore.green}\nEnter the function you would like to enter: {Style.reset}\n"
#         )
#         clear_console()

#         try:
#             user_selection = int(user_selection)
#             if user_selection < 1 or user_selection > 5:
#                 raise ValueError
#         except ValueError:
#             clear_console()
#             print(
#                 f"{Fore.red}Please enter a valid number between 1 and 5:{Style.reset}\n"
#             )
#         if user_selection == 1:
#             clear_console()
#             we_menu()
#         elif user_selection == 2:
#             clear_console()
#             wt_menu()
#         elif user_selection == 3:
#             clear_console()
#             el_menu()
#         elif user_selection == 4:
#             clear_console()
#             pw_menu()
#     print(f"{Fore.red}Quitting the application...{Style.reset}")


# display_menu()
