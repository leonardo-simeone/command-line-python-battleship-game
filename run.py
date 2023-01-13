import random  # Import random module


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
        print("   ABCDEFGH")
        print("  +-+-+-+-+")
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
            print("That's not even in the ocean 🤔")
            return Battleship.get_user_input(self)

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


def run_game():
    """
    Function to run the game utilizing the Gameboard and Battleship classes
    and their corresponding methods
    """
    print("🚢 Let's Play Battleship!🚢\n")
    print("🧾 RULES 🧾:\n")
    print("- There are 5 battleships 🚢 hidden in the board.")
    print("- You have 20 missiles 🚀 to sink them all.")
    print("- If you sink all 5 battleships before running out")
    print("  of missiles you win!")
    print("- You must choose your missiles coordinates by selecting")
    print("  a row in the board between 1 and 8 as well as a column")
    print("  between A and H.\n")
    computer_board = GameBoard([["⬛"] * 8 for i in range(8)])
    user_guess_board = GameBoard([["⬛"] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)

    # start 20 turns
    turns = 20
    while turns > 0:
        GameBoard.print_board(user_guess_board)
        # get user input
        user_x_row, user_y_column = Battleship.get_user_input(object)

        # check if user's duplicate guess
        while user_guess_board.board[user_x_row][user_y_column] == "❌" or user_guess_board.board[user_x_row][user_y_column] == "🚢":  # noqa
            print("You shot a missile to that coordinate already! 🖐")
            user_x_row, user_y_column = Battleship.get_user_input(object)

        # check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "🚢":
            print("🔥You sunk 1 of my battleships!🔥")
            user_guess_board.board[user_x_row][user_y_column] = "🚢"

        else:
            print("You missed! 😣")
            user_guess_board.board[user_x_row][user_y_column] = "❌"

        # check for win or lose
        if Battleship.count_destroyed_ships(user_guess_board) == 5:
            print("CONGRATULATIONS! You hit all 5 battleships!🎉🎈")
            GameBoard.print_board(user_guess_board)
            break

        # let the user know how many turns are left
        else:
            turns -= 1
            print(f"You have {turns} 🚀 missiles remaining")

            if turns == 0:
                print("Sorry you ran out of missiles")
                GameBoard.print_board(user_guess_board)
                break


run_game()
