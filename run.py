import os
import random  # Import random module


def clear():
    """
    clear function to clean up the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


class GameBoard:
    """
    Create an object of an entity board. This class
    will create 2 objects, the user's board and the computer's
    board. It also has methods that will allow to print the user's board
    while keeping the computer's hidden and return the column value to the
    user's input key by using the letters_to_numbers dictionary.
    """

    def __init__(self, board):
        self.board = board

    def convert_letters_to_numbers():
        """
        Method used to return the user's
        input key utilizing a dictionary
        """
        letters_to_numbers = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
            "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        """
        Method used to print the user's board
        """
        print("   A B C D E F G H")
        print("  +-+-+-+-+-+-+-+-")
        row_number = 1
        for row in self.board:
            print("%d|%s" % (row_number, " ".join(row)))
            row_number += 1


class Battleship:
    """
    Create battleship objects in a board entity. This class
    will create 5 battleships. Via its methods it will add them
    to the hidden computer's board,
    it will get and return the user's inputs for row and column,
    it will handle any user input errors, return the user input
    and count the hit battleships.
    it will also handle the game intro (welcoming), giving the
    user the option to print (see/read) the rules or to start
    the game right away.
    """

    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """
        Method used to create the computer's ships
        and add them to the computer's hidden board
        """
        for i in range(5):
            computer_x_row = random.randint(0, 7)
            computer_y_column = random.randint(0, 7)

            while self.board[computer_x_row][computer_y_column] == "🚢":
                computer_x_row = random.randint(0, 7)
                computer_y_column = random.randint(0, 7)
            self.board[computer_x_row][computer_y_column] = "🚢"
        return self.board

    def get_user_input(self):
        """
        Method used to get the user's inputs, row and column
        it will also handle user's input errors
        """
        try:
            user_x_row = input("Enter the row of the ship: \n")
            while user_x_row not in '1,2,3,4,5,6,7,8':
                print(
                    f'{user_x_row} is not an appropriate choice, '
                    'please select a row between 1 and 8')
                user_x_row = input("Enter the row of the ship: \n")

            user_y_column = input("Enter the column of the ship: \n").upper()
            while user_y_column not in 'A,B,C,D,E,F,G,H':
                print(
                    f'{user_y_column} is not an appropriate choice, '
                    'please select a column between A and H')
                user_y_column = input(
                    "Enter the column of the ship: \n").upper()
            return int(user_x_row) - 1, GameBoard.convert_letters_to_numbers()[user_y_column]  # noqa
        except Exception as e:
            print("That's not even in the ocean🤔")
            return Battleship.get_user_input(self)

    def intro_to_game(self):
        """
        Method used to get the user's inputs, to select
        whether they want to read the rules and start the
        game or simply start the game
        """
        try:
            user_choice = input(
                "To see the rules press 'R'\n"
                "To start the game press 'G': \n").upper()
            while user_choice not in 'R,G':
                print(
                    f"{user_choice} is not a valid option please select "
                    "an option between 'R' and 'G'")
                user_choice = input(
                    "To see the rules press 'R'\n"
                    "To start the game press 'G': \n").upper()

        except Exception as e:
            print("Please select a valid option")
            return Battleship.intro_to_game(self)

        if user_choice == "R":
            print_rules()
            run_game()

        if user_choice == "G":
            clear()
            run_game()

        if user_choice == "":
            print("Please select a valid option")
            Battleship.intro_to_game(self)

    def count_destroyed_ships(self):
        """
        Method used to count how many ships from the hidden
        computer's board the user has hit
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "🚢":
                    hit_ships += 1
        return hit_ships


def print_intro():
    """
    Function to print the welcome message to the user and
    offer them the options from intro_to game function
    """
    print(
        "Hello and Welcome to: \n"
        "🚢  Battleship Game 🚢\n"
        "🔧 Built in python🔧\n"
        "by Leonardo Simeone 👦\n"
        "To start the game please\n"
        "select one of the two options\n"
        "below 👇 :\n")


def print_rules():
    """
    Function to print the game rules should the user
    select to do so
    """
    clear()
    print(
        "🧾  RULES 🧾 :\n"
        "* There are 5 battleships 🚢\n"
        "  hidden in the board.\n"
        "* You have 20 missiles 🚀\n"
        "* To win, sink them all before\n"
        "  running out of missiles.\n"
        "* Choose your missiles\n"
        "  coordinates by selecting a\n"
        "  row between 1 and 8, also\n"
        "  a column between A and H.\n")


def run_game():
    """
    Function to run the game utilizing the Gameboard and Battleship classes
    and their corresponding methods as well as complement functions
    """
    print("🚢  Let's Play Battleship! 🚢\n")
    computer_board = GameBoard([["⬛"] * 8 for i in range(8)])
    user_guess_board = GameBoard([["⬛"] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)

    # start 20 turns
    turns = 20
    while turns > 0:
        GameBoard.print_board(user_guess_board)
        user_x_row, user_y_column = Battleship.get_user_input(object)
        clear()

        # check if user's duplicate guess
        while user_guess_board.board[user_x_row][user_y_column] == "❌" or user_guess_board.board[user_x_row][user_y_column] == "🚢":  # noqa
            print(
                "You fired a missile to that\n"
                "coordinate already!🖐")
            GameBoard.print_board(user_guess_board)
            user_x_row, user_y_column = Battleship.get_user_input(object)
            clear()

        # check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "🚢":
            print("🔥 You sunk 1 of my battleships!🔥")
            user_guess_board.board[user_x_row][user_y_column] = "🚢"

        else:
            print("You missed! 😣")
            user_guess_board.board[user_x_row][user_y_column] = "❌"

        # check for win or lose
        if Battleship.count_destroyed_ships(user_guess_board) == 5:
            print("CONGRATULATIONS! You hit all 5 battleships!🎉🎈")
            GameBoard.print_board(user_guess_board)
            print("You've Won!")
            return play_again_option()

        # let the user know how many turns are left
        else:
            turns -= 1
            print(f"You have {turns} 🚀  missiles remaining")

            if turns == 0:
                print("Sorry you ran out of missiles")
                GameBoard.print_board(user_guess_board)
                play_again_option()


def play_again_option():
    """
    Function to ask the user once they've finished
    the game whether they want to play again or
    end the program
    """
    try:
        play_again = input(
            "\nDo you want to play again? \n"
            "press 'Y' for yes or 'N' for no: \n").upper()
        while play_again not in 'Y,N':
            print(
                f"{play_again} is not a valid option please select "
                "an option between 'Y' and 'N'")
            play_again = input(
                "\nDo you want to play again? "
                "press 'Y' for yes or 'N' for no: \n").upper()

    except Exception as e:
        print("Please select a valid option")
        return play_again

    if play_again == "Y":
        clear()
        run_game()

    if play_again == "N":
        return print("Thanks for Playing!")

    if play_again == "":
        print("Please select a valid option")
        return play_again_option()


print_intro()
Battleship.intro_to_game(object)
