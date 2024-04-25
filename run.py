# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import pyfiglet
import time
import gspread
from google.oauth2.service_account import Credentials
from questions import nfl_questions

#The scope below lists the APIs that my program should access in order to run
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

#Eveything to do with google credentials below are copied from Code Institute Love Sandwiches project
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('NFL_Quiz')

#This function adds the ability to clear the terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function to start the game, 
def game_start():

    clear()
    start_text = pyfiglet.figlet_format("N F L  Q U I Z", font="3-d")
    print(start_text)
    game_menu()


#Game menu presenting you with the 'NFL Quiz' figlet, aswell as three options whether you want to start the game, see the leader board or see the rules.
def game_menu():
    print("Welcome to a 'NFL Quiz' the game that will test your knowledge about NFL trivia\n")
    print("Type 'S/s' to start the quiz, 'L/l' to see the leaderboard or 'R/r' to see the rules")
    print("""
    -       'S/s' Start Quiz        -
    -       'L/l' Leaderboard       -
    -       'R/r' Game Rules        -\n""")


game_start()