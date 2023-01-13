import random # Import random module


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
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                              "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        """ 
        Method used to print the user's board
        """
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """
    Create battleship objects in a board entity. This class
    will create 5 battleships. Via its methods it will add them
    to the hidden computer's board, it will get and return the user's inputs for
    row and column, it will handle any user input errors, return the user input
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

            while self.board[computer_x_row][computer_y_column] == "X":
                computer_x_row = random.randint(0, 7)
                computer_y_column = random.randint(0, 7)
            self.board[computer_x_row][computer_y_column] = "X"
        return self.board
    

    def get_user_input(self):
        """
        Method used to get the user's inputs, row and column
        it will also handle user's input errors
        """
        try:
            user_x_row = input("Enter the row of the ship: ")
            while user_x_row not in '1,2,3,4,5,6,7,8':
                print(f'{user_x_row} is not an appropriate choice, please select a row between 1 and 8')
                user_x_row = input("Enter the row of the ship: ")

            user_y_column = input("Enter the column of the ship: ").upper()
            while user_y_column not in 'A,B,C,D,E,F,G,H':
                print(f'{user_y_column} is not an appropriate choice, please select a column between A and H')
                user_y_column = input("Enter the column of the ship: ").upper()
            return int(user_x_row) - 1, GameBoard.convert_letters_to_numbers()[user_y_column]
        except Exception as e:
            print("That's not even in the ocean")
            return Battleship.get_user_input(self)
    
    def count_destroyed_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships

user_guess_board = GameBoard([[" "] * 8 for i in range(8)])

user_guess_board.board[3][0] = "X"
user_guess_board.board[5][3] = "X"
user_guess_board.board[0][6] = "X"
user_guess_board.print_board()
print(" ")
print(Battleship.count_destroyed_ships(user_guess_board))

