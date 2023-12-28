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