# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import pyfiglet
import time
import gspread
import random
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
    print("Welcome to a 'NFL Quiz' the game that will test your knowledge")
    print("about NFL trivia\n")
    print("Type 'S/s' to start the quiz, 'L/l' to see the leaderboard")
    print("or 'R/r' to see the rules")
    print("""
    -       'S/s' Start Quiz        -
    -       'L/l' Leaderboard       -
    -       'R/r' Game Rules        -\n""")
    menu_options()


#Menu with options to either start the game, see the leadwerboard or to see the rules
def menu_options():
    try:
        while True:
            option = input().upper()
            if option not in ["S", "L", "R"]:
                raise ValueError
            else:
                if option == 'S':
                    select_questions()
                    break
                elif option == 'L':
                    leaderboard()
                    break
                elif option == 'R':
                    rules()
                    break
    except ValueError:
        clear()
        print("Input error! You did not type 'S/s', 'L/l' or 'R/r'")
        print("Please type one of the following: 'S/s' for ")
        print("Start Quiz,'L/l' for Leaderboard or")
        print("'R/r' to see the Rules.\n")
        time.sleep(3)
        game_menu()


def select_questions():
    clear()
    while True:
        num_questions = input("How many questions do you want to answer? (5 or 10):\n")
        if num_questions in ['5', '10']:
            num_questions = int(num_questions)
            break
        else:
            print("Invalid input! Please choose 5 or 10.")

    questions = random.sample(nfl_questions, num_questions)

    correct_answers = 0
    for idx, question in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {question['question']}")
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")

        while True:
            user_answer = input("Your answer:\n")
            if user_answer.isdigit() and int(user_answer) in [1, 2]:
                user_answer = int(user_answer) - 1
                break
            else:
                print("Invalid input! Please type 1 or 2.")

        if question['options'][user_answer] == question['correct']:
            print("Correct! You get 1 point")
            correct_answers += 1
        else:
            print("Incorrect!")
            print(f"The correct answer was: {question['correct']}")
        time.sleep(2)

    print(f"\nYou answered {correct_answers} out of {num_questions} questions correctly.\n")
    time.sleep(2)
    ask_to_leaderboard(num_questions, correct_answers)