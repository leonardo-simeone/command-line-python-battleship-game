import random # Import random module
class GameBoard:

    def __init__(self, board):
        self.board = board

    # Method used to return the user's input key utilizing a dictionary
    def convert_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                              "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    # Method used to print the user's board
    def print_board(self):
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
print(user_guess_board.print_board())

print(GameBoard.convert_letters_to_numbers()["C"])