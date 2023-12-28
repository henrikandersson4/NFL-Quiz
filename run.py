# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import pyfiglet

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# User Interface Functions
def display_welcome_screen():
    clear()
    print("")
    nfl_text = pyfiglet.figlet_format("NFL QUIZ", font="3-d")
    print(nfl_text)
    display_game_menu()

#Displaying the game menu
def display_game_menu():
    print("Are you ready for some NFL questions?\n")
    print("Choose Start Quiz, Leaderboard, or Game Rules below:")
    print("""
    -        Start Quiz        -
    -        Leaderboard       -
    -        Game Rules        -\n""")
    print("Instructions:")
    print("Type 's or S' to Start the Quiz, 'l or L'"
          "for Leaderboard, or 'r or R' for Game Rules.")
    handle_menu_selection()

# Function to handle game menu input
def handle_menu_selection():
    try:
        while True:
            option = input("\n").upper()
            if option not in ["S", "L", "R"]:
                raise ValueError
            else:
                if option == 'S':
                    start_quiz()
                    break
                elif option == 'L':
                    show_leaderboard()  # Adjusted function call
                    break
                elif option == 'R':
                    show_game_rules()  # Adjusted function call
                    break
    except ValueError:
        clear()
        print("Invalid input! Choose 's or S' for Start Quiz, 'l or L'"
              "for Leaderboard, or 'r or R' for Game Rules.")
        print("Please type the correct option.\n")
        display_game_menu()

#Function to show the game rules
def show_game_rules():
    clear()
    print("Welcome to Game Rules!")
    print("""
        This quiz consists of 5 or 10 questions, and the answer for each
        question will be either one of two options that are displayed
        underneath. You will have to Type either '1' or '2' to select
        the answer you think is the correct one and press Enter.
        The quiz will continue until all questions have been played
        for the selected amount of questions. Good luck!\n""")
    print("Type 'm or M' to return to the Menu.")
    try:
        while True:
            back_to_menu = input("\n").upper()
            if back_to_menu not in ["M"]:
                raise ValueError
            else:
                clear()
                display_game_menu()
    except ValueError:
        clear()
        print("Did you really press 'm or M'? Try again!")
        time.sleep(3)
        show_game_rules()


