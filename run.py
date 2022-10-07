from random import randint


class Gameboard:
    """
    This class includes the main board, and two instances
    of game boards for both the player and the computer.
    It includes the board size, the players name, type of board,
    and the number of ships. It includes the methods for adding ships,
    guesses and printing the board to the user.
    """

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.num_ships = 4
        self.board = [["." for x in range(5)] for y in range(5)]
        self.guesses = []
        self.shiploc = []

    # Function is based on Code Institute Portfolio Project Scope video
    def print(self):
        """
        This function displays the board to the player
        """
        for row in self.board:
            print(" ".join(row))

    def add_ship(self, x_cord, y_cord):
        """
        Adds ships to shiplocations list and shows
        location of ship on playersboard.
        """

        if self.type == "Player":
            self.shiploc.append((x_cord, y_cord))
            self.board[x_cord][y_cord] = "@"
        else:
            self.shiploc.append((x_cord, y_cord))
 
    def guess(self, x_cord, y_cord):
        """
        Stores guesses and compares to ship location
        """

        self.board[x_cord][y_cord] = "X"

        if (x_cord, y_cord) in self.shiploc:
            self.board[x_cord][y_cord] = "H"
            print("It's a hit!")
        else:
            print("Ai, missed!")


def populate_board(board):
    """
    Creates 2 random numbers to create coordinate.
    Each coordinate is added to shiplocation list of instance.
    """
    x_cord = randint(0, 4)
    y_cord = randint(0, 4)
    board.add_ship(x_cord, y_cord)


def valid_cord(players_board, computer_board, x_cord, y_cord):
    """
    Validates the coordinates against earlier guesses.
    If validation is succesful it appends guess, to guesses
    """
    if (x_cord, y_cord) in players_board.guesses:
        print("You already guessed this location, try another")
        return True
    else:
        players_board.guesses.append((x_cord, y_cord))
        computer_board.guess(x_cord, y_cord)
        print(players_board.guesses)
        return False


def computer_guess(computer_board, players_board):
    """
    Creates a random guess for the computer,
    and appends it to the computer's guesses
    """
    while True:
        x_cord = randint(0, 4)
        y_cord = randint(0, 4)
        if (x_cord, y_cord) in computer_board.guesses:
            continue
        else:
            computer_board.guesses.append((x_cord, y_cord))
            players_board.guess(x_cord, y_cord)
            print(computer_board.guesses)
            return False


def start_game(player_name, players_board, computer_board):
    """
    This starts the new game.
    It displays the boards and let the player input its guesses
    """
    
    print(f"{player_name} this is your board:\n")
    players_board.print()
    print("-" * 30)
    print("This is the computer's board:")
    computer_board.print()
    
    while True:
        try:
            while True:
                try:
                    guess_row = int(input("Guess a row in range 0-4:\n"))
                except ValueError:
                    print("That's not a number, try again")
                else:
                    if guess_row in range(0, 5):
                        break
                    else:
                        print("Out of range. Try again")

            while True:
                try:
                    guess_column = int(input("Guess a column between 0-4:\n"))
                except ValueError:
                    print("That's not a number, try again")
                else:
                    if guess_column in range(0, 5):
                        break
                    else:
                        print("Out of range. Try again")
            valid_cord(players_board, computer_board, guess_row, guess_column)
        except ValueError:
            print("You already made this guess, try again")
        computer_guess(computer_board, players_board)
        players_board.print()
        computer_board.print()


def new_game():
    """
    Starts a new game. It start by resetting the scores,
    it displays the boards, and will initialize the start of the game.
    """

    player_name = input("Enter your name please: \n")
    print("-" * 30)
    print(f"Hi, {player_name}\n")
    print("The board grid is 5*5 and the number of ships is 4!\n")
    print("Be aware, the top left corner is row: 0, col: 0\n")

    players_board = Gameboard(player_name, type="Player")
    computer_board = Gameboard("Computer", type="Computer")

    for i in range(4):
        populate_board(players_board)
        populate_board(computer_board)
    print(f"Computers loc: {computer_board.shiploc}")
    print(f"Players board: {players_board.shiploc}")
    start_game(player_name, players_board, computer_board)


print("WELCOME! ARE YOU READY TO BATTLE?\n")


new_game()
