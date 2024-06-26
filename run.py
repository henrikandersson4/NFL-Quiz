import os
import pyfiglet
import time
import gspread
import random
from google.oauth2.service_account import Credentials
from questions import nfl_questions


# The scope below lists the APIs that my program should access in order to run
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


"""
Eveything to do with google credentials below are copied from
Code Institute Love Sandwiches project
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('NFL_Quiz')


def clear():
    """
    This function adds the ability to clear the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def game_start():
    """
    Function to start the game
    """
    clear()
    start_text = pyfiglet.figlet_format("N F L  Q U I Z", font="3-d")
    print(start_text)
    game_menu()


def game_menu():
    """
    Game menu presenting you with the 'NFL Quiz' figlet, aswell as three
    options whether you want to start the game, see the leader board or
    see the rules.
    """
    print("Welcome to a 'NFL Quiz' the game that will test your knowledge")
    print("about NFL trivia\n")
    print("Type 'S/s' to start the quiz, 'L/l' to see the leaderboard")
    print("or 'R/r' to see the rules")
    print("""
    -       'S/s' Start Quiz        -
    -       'L/l' Leaderboard       -
    -       'R/r' Game Rules        -\n""")
    menu_options()


def menu_options():
    """
    Menu with options to either start the game, see the
    leadwerboard or to see the rules
    """
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
        num_questions = input("How many questions do you want? (5 or 10):\n")
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


def rules():
    clear()
    print("NFL Quiz Rules!\n")
    print("This quiz consists of 5 or 10 questions. Each question will")
    print("give you two options")
    print("'1' or '2' to choose from. To select an option,")
    print("you type either '1' or '2' depending")
    print("on which one you think is correct. Only one of the options")
    print("is correct, so think before")
    print("you answer!\n")
    print("Type 'M/m' to return to the Menu.")
    try:
        while True:
            back_to_menu = input("\n").upper()
            if back_to_menu not in ["M"]:
                raise ValueError
            else:
                clear()
                game_menu()
    except ValueError:
        clear()
        print("Did you really press 'M/m'? Try again!")
        time.sleep(2)
        rules()


def get_score_from_sheet(sheet_name):
    worksheet = SHEET.worksheet(sheet_name)
    data = worksheet.get_all_values()[1:]  # Skips the header row in sheet

    try:
        data = sorted(data, key=lambda x: int(x[1]), reverse=True)
    except ValueError as e:
        print(f"Error sorting data: {e}")
        return []

    return data


def display_leaderboard(data, description):
    print(f"{description}:\n")
    leaders = min(len(data), 3)
    for i in range(leaders):
        print(f"{i + 1}) {data[i][0]} {data[i][1]} Points\n")
    print("")


def leaderboard():
    clear()
    print("Contacting database...")
    time.sleep(0.8)
    print("Loading score from database...")
    time.sleep(1.5)
    clear()
    print("******* Leaderboard *******\n")

    leader_five = get_score_from_sheet('fiveq')
    leader_ten = get_score_from_sheet('tenq')

    display_leaderboard(leader_five, "5 Questions")
    display_leaderboard(leader_ten, "10 Questions")

    print("Return to menu, Type 'm or M'")
    while True:
        back_to_menu = input("\n").upper()
        if back_to_menu == "M":
            clear()
            game_menu()
            break
        else:
            clear()
            print("Did you really press 'm or M'? Try again!")


def ask_to_leaderboard(num_questions, correct_answers):
    if num_questions == 5 and correct_answers <= 2:
        print("Better luck next time!")
        time.sleep(2)
        end_game()
    elif num_questions == 10 and correct_answers <= 4:
        print("Better luck next time!")
        time.sleep(2)
        end_game()
    else:
        print("Nice job!")
        print("Do you want to submit your score to the leaderboard?")
        print("Input Y/y for yes and N/n for no")
        while True:
            submit_to_leaderboard = str(input("Y or N:\n")).upper()
            if submit_to_leaderboard not in ["Y", "N"]:
                print(""""Invalid input! Please input only 'Y/y' or 'N/n'""")
            else:
                if submit_to_leaderboard == "Y":
                    name(correct_answers, num_questions)
                elif submit_to_leaderboard == "N":
                    clear()
                    end_game()
                break


def name(correct_answers, num_questions):
    print("\nPlease type a name using no more than 10 characters containing")
    print("only letters and/or numbers")
    try:
        while True:
            player_name = str(input("Input a name:\n"))
            if len(player_name) <= 10 and player_name.isalnum():
                print(f"Thank you {player_name}!")
                print("Contacting database...")
                time.sleep(0.4)
                print("Uploading score to database...")
                time.sleep(1.5)
                print("Upload finished. Thank you for playing!")
                player_to_leaderboard(correct_answers, num_questions, player_name)
                time.sleep(1)
                return player_name
            else:
                raise ValueError
    except ValueError:
        print("Did you input a name no longer than 10 characters and")
        print("only containing letters and/or numbers?")
        print("Please try again!\n")
        time.sleep(3)
        clear()
        name(correct_answers, num_questions)


def player_to_leaderboard(correct_answers, num_questions, player_name):
    if num_questions == 5:
        player_points_five = SHEET.worksheet('fiveq')
        player_points_five.append_row([player_name, correct_answers])
        clear()
        end_game()
    elif num_questions == 10:
        player_points_ten = SHEET.worksheet('tenq')
        player_points_ten.append_row([player_name, correct_answers])
        clear()
        end_game()


def end_game():
    print("Do you want to play again?")
    print("Type 'Y/y' for yes or")
    print("'N/n' for no and exit the game")
    while True:
        try:
            players_choice = str(input("Y or N:\n")).upper()
            if players_choice not in ["Y", "N"]:
                raise ValueError
            else:
                if players_choice == "Y":
                    clear()
                    game_start()
                elif players_choice == "N":
                    clear()
                    print("Than you for this time!")
                    time.sleep(0.8)
                    print("Shuting down...")
                    time.sleep(2)
                    clear()
                    exit(0)
        except ValueError:
            print("Invalid input! Please input only 'Y/y' or 'N/n'")


def main():
    game_start()


if __name__ == "__main__":
    main()
