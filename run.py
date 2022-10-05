from random import randint


class Gameboard:
    """
    This class includes the main board, and two instances
    of game boards for both the player and the computer. 
    It includes the board size, the players name, type of board, 
    and the number of ships. It includes the methods for adding ships, 
    guesses and printing the board to the user.
    """

    def __init__(self, name, btype):
        self.name = name
        self.btype = btype
        self.num_ships = 4
        self.board = [["." for x in range(5)] for y in range(5)]
        self.guesses = []
        self.shiploc = []
    
    # This code is copied from Code Institute Portfolio Project Scope video
    def print(self):
        for row in self.board:
            print(" ".join(row))


def populate_board(players_board):
    new_ship_loc = []
    for i in range(2):
        cord = randint(0, 4)
        new_ship_loc.append(cord)
    players_board.shiploc.append(new_ship_loc)


def new_game():
    """
    Starts a new game. It start by resetting the scores, 
    it displays the boards,
    and will initialize the start of the game.
    """
    
    player_name = input("Enter your name please: \n")
    print("-" * 30)
    print(f"Hi, {player_name}\n")
    print("The board grid is 5*5 and the number of ships is 4!\n")
    print("Be aware, the top left corner is row: 0, col: 0\n")

    players_board = Gameboard(player_name, btype="Player")
    
    for i in range(4):
        populate_board(players_board)
    print(players_board.shiploc)


print("WELCOME! ARE YOU READY TO BATTLE?\n")


new_game()
