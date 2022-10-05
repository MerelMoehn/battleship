
class Gameboard:
    """
    This class includes the main board, and two instances
    of game boards for both the player and the computer. 
    It includes the board size, the players name, type of board, 
    and the number of ships. It includes the methods for adding ships, 
    guesses and printing the board to the user.
    """

    def __init__(self, name, btype):
        self.num_ships = 4
        self.board = [["." for x in range(5)] for y in range(5)]
        self.name = name
        self.btype = btype

