from random import randint
import os

scores = {"Player": 0, "Computer": 0}


# part of this class is based on Code Institute Portfolio Project Scope video
class GamePlayer:
    """
    This class includes a general Player, and two instances
    of players for both the player and the computer.
    It includes the board size, the players name, type of board,
    and the number of ships. It includes the methods for adding ships,
    guesses and printing the board to the user.
    """

    def __init__(self, ptype):
        self.ptype = ptype
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
            print(" " + " ".join(row))

    # Function is partly based on Code Institute Portfolio Project Scope video
    def add_ship(self, x_cord, y_cord):
        """
        Adds ships to shiplocations list and shows
        location of ship on playersboard.
        """

        if self.ptype == "Player":
            self.shiploc.append((x_cord, y_cord))
            self.board[x_cord][y_cord] = "@"
        else:
            self.shiploc.append((x_cord, y_cord))

    def guess_handling(self, x_cord, y_cord):
        """
        Stores guesses and compares to ship location
        """
        self.board[x_cord][y_cord] = "X"

        if (x_cord, y_cord) in self.shiploc:
            self.board[x_cord][y_cord] = "H"
            if self.ptype == "Computer":
                print(" Well done, It's a hit!")
            else:
                print(" The computer hit one of your ships!")
            keep_score(self.ptype)
        else:
            if self.ptype == "Computer":
                print(" You missed!")
            else:
                print(" Lucky you, the computer missed!")


def populate_board(board):
    """
    Creates 2 random numbers to create coordinate.
    Each coordinate is added to shiplocation list of instance.
    """

    while len(board.shiploc) < 4:
        x_cord = randint(0, 4)
        y_cord = randint(0, 4)
        if (x_cord, y_cord) in board.shiploc:
            continue
        board.add_ship(x_cord, y_cord)


def valid_cord(game_player, game_computer, x_cord, y_cord):
    """
    Validates the coordinates against earlier guesses.
    If validation is succesful it appends guess, to guesses
    """
    if (x_cord, y_cord) in game_player.guesses:
        print(" You already guessed this location, try another")
        return True
    else:
        game_player.guesses.append((x_cord, y_cord))
        os.system("clear")
        game_computer.guess_handling(x_cord, y_cord)
        return False


def computer_guess(game_computer, game_player):
    """
    Creates a random guess for the computer,
    and appends it to the computer's guesses
    """
    while True:
        x_cord = randint(0, 4)
        y_cord = randint(0, 4)
        if (x_cord, y_cord) in game_computer.guesses:
            continue
        else:
            game_computer.guesses.append((x_cord, y_cord))
            game_player.guess_handling(x_cord, y_cord)
            return False


def keep_score(ptype):
    """
    Adds a point to the score if Player or Computer has a hit
    """
    if ptype == "Computer":
        scores["Player"] += 1
    elif ptype == "Player":
        scores["Computer"] += 1
    else:
        print(" No score can be added")


def calculate_winner(player_name):
    """
    Calculates whether there is a winner or not.
    """
    if scores["Computer"] == 4:
        print(" GAME OVER! The computer won")
        return False
    elif scores["Player"] == 4:
        print(f" YOU WON! Congratulations {player_name}!")
        return False
    else:
        return True


def show_board(player_name, game_player, game_computer):
    """
    Prints the current board status of both computer and player.
    """
    print(f" {player_name} this is your board:\n")
    game_player.print()
    print(" " + "-" * 30)
    print(" This is the computer's board:\n")
    game_computer.print()
    print(" " + "-" * 30)


def reset_game():
    """
    Asks the user if he wants to reset the game or not.
    If user wants to resets it will reset the score and,
    restart the game.
    """

    while True:
        try:
            reset_input = input(" Do you want to reset the game?"
                                "(Yes or No)\n")
            if reset_input == "Yes" or reset_input == "No":
                break
            else:
                raise ValueError()
        except ValueError():
            print(" Please enter Yes/No")
    if reset_input == "Yes":
        scores["Player"] = 0
        scores["Computer"] = 0
        os.system("clear")
        new_game()
    else:
        os.system("clear")
        print(" Alright, goodbye!")


def input_row():
    while True:
        try:
            input_row = int(input(" Guess a row in range 0-4:\n"))
        except ValueError:
            print(" That's not a number, try again")
        else:
            if input_row in range(0, 5):
                return input_row
                break
            else:
                print(" Out of range. Try again")


def input_column():
    while True:
        try:
            input_column = int(input(" Guess a column between 0-4:\n"))
        except ValueError:
            print(" That's not a number, try again")
        else:
            if input_column in range(0, 5):
                return input_column
                break
            else:
                print(" Out of range. Try again")


def start_game(player_name, game_player, game_computer):
    """
    This starts the new game.
    It displays the boards and let the player input its guesses
    """
    show_board(player_name, game_player, game_computer)

    while True:
        try:
            guess_row = input_row()
            guess_column = input_column()

            if valid_cord(game_player, game_computer,
                          guess_row, guess_column):
                continue

        except ValueError:
            print(" You already made this guess, try again")

        computer_guess(game_computer, game_player)

        print(" " + "-" * 30)
        print(f" {player_name}'s hit rate: {scores['Player']}\n"
              f" Computer's hit rate: {scores['Computer']} ")
        print(" " + "-" * 30)

        show_board(player_name, game_player, game_computer)

        if not calculate_winner(player_name):
            break

    reset_game()


def new_game():
    """
    Starts a new game. It start by resetting the scores,
    it displays the boards, and will initialize the start of the game.
    """
    while True:
        try:
            player_name = input(" Enter your name please: \n")
            if str.isalpha(player_name):
                break
            else:
                raise ValueError()
        except ValueError:
            print(" Is this really a name? Try again")

    print(" " + "-" * 30)
    print(f" Hi, {player_name}\n")
    print(" The board grid is 5*5 and the number of ships is 4!\n")
    print(" Be aware, the top left corner is row: 0, col: 0\n")
    print(" If you hit, you will see an 'H' on the computer's board")
    print(" If you miss, you will see an 'X' on the board")

    game_player = GamePlayer(ptype="Player")
    game_computer = GamePlayer(ptype="Computer")

    populate_board(game_player)
    populate_board(game_computer)
    start_game(player_name, game_player, game_computer)


print(" WELCOME TO BATTLESHIP! ARE YOU READY TO BATTLE?\n")


new_game()
