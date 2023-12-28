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