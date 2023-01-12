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

    
computer_board = GameBoard([[" "] * 8 for i in range(8)])

print(Battleship.create_ships(computer_board))

print(GameBoard.convert_letters_to_numbers()["C"])