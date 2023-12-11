print(
    f"Welcome the the Workout Tracker application. Please select from the following options:\n"
)


def display_menu():
    user_selection = ""
    while user_selection != 7:
        print("[ 1 ] Enter Workout Entry")
        print("[ 2 ] Create Custom Workout Template")
        print("[ 3 ] View Existing Workout Templates")
        print("[ 4 ] Edit Existing Workout Templates")
        print("[ 5 ] View Exercise List Database")
        print("[ 6 ] View Previous Workout Entries")
        print("[ 7 ] Exit the Program")
        user_selection = input("\nEnter the function you would like to enter: \n")

        try:
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > 7:
                raise ValueError
        except ValueError:
            print("\nPlease enter a valid number between 1 and 7: \n")

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
