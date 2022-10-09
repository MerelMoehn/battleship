![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

#LET'S PLAY BATTLESHIP

Welcome USER_NAME,

In this document I will explain the approach and instructions for the BattleShip game. The purpose of this project is let the user enjoy an online game called Battleship. The goal of the game is to defeat the computer sinking his ships. Though, the player must be quick because otherwise the bank may sink all of the player's ship. 

The last update to this file was: **Oktober 10, 2022**

## Deployed project
The game can be played via the following link: https://battleship-mm.herokuapp.com/

## User Stories
**User stories**
The user stories that are at the base of this website are as follows:

* As a user I want to play the online version of Battleship
* As a user I want to understand how this game works

## Instructions and features
This is an online version of the Battleship game. For who is unfamiliar with the game, please read more about if via the following link: https://en.wikipedia.org/wiki/Battleship_(game)

In this version the player is asked to enter his or her name to personalize the game.
After the player inserts his name the game will start and the instructions are displayed

Two random boards are generated for both the player and the computer. The locations of the player's ships are shown by a '@'.
The location of the computer's ship are hidden.

The player is asked to guess a row, and hence guess a column. If the input is not valid, the user gets feedback and can try again.
A hit is displayed by an 'H' and a miss is displayed by a 'X'.

The player wins if the sinks the 4 ships of the computer before the computer sinks the player's 4 ships. 

After the player wins or loses, he can choose to reset the game.

**Features**

![Image of user input](./assets/images/userinput.png)
* User input: the user can insert his guess for a row and column.

![Image of input validation](./assets/images/userfeedback.png)
* Input validation: the player gets feedback when the input is not valid. The validation checks for range(0-4), type(number), and if the guess has already been made before.

![Image of score board](./assets/images/scoreboard.png)
* Score board: to give the player a quick overview of the scores instead of counting the H's, a score board is displayed with the hit rate of both player and computer.

![Image of boards](./assets/images/displayboard_hitsandmisses.png)
* Boards: both the player's board and the computer's board are displayed. An 'H" represents a HIT, an X represents a MISS. The location of the player's ships are represented by an @. The computer's ships are hidden.

* Result: after 4 ships are sunk by either the player or the computer, the game will display a result message.

## Data model
In this project I use a Board class model. There are two instances of the Board class model: the Players Board and the Computer Board. 

The Board class model stores the type of the board (player or computer), number of ships, the guesses that are made, and the ship locations.

The class also includes several methods:
* The print method: this method prints the board. The code for this method is based on the CodeInstitute scope model project.
* The add ship method: this methods adds a ship to the board by taking the random generated coordinates as parameters.
* The guess_handling method: this method checks whether the guess results in a HIT or in a MISS, and calls the keep_score function in case of a HIT.


## Testing
**Validators**
PEP8 was installed via the following steps:
* I rann the command pip3 install pycodestyle.
* In my workspace, I pressed Cmd+Shift+P on Mac.
* I typeed the word linter into the search bar, and clicked on Python: Select Linter.
* I selected pycodestyle from the list.
No errors were red underlined and no errors were shown in the PROBLEM tab besides:
![Image of problem tab](./assets/images/warnings_problemtab.png)


**Testing the User Stories from User Experience (UX) section**
* As a user I want to play the online version of Battleship: the user can play the online version of this Battelship game via Heroku. The user is able to make a guess for a row and a column to try and hit one of the computer's ships. If the user sinks four of the computer's ships before the computer sinks all of his ships, the user wins.
* As a user I want to understand how this game works: the user sees the instructions of the game when the game starts. Step by step the user is asked to make a guess. If the user input is not valid, the user receives feedback why it is invalid, and the user can try again.

**Bugs found and solved**
* Break while True loop 1: there was a bug that did not continue the while True loop after the user inserted a number outside of the scope. This was fixed by adding a return value and using that to break the while loop.
* Break while True loop 2: there was a bug that kept the game running even though there was a winner. This was fixed by using the return value in an if statement and letting the loop break after the return was False.
* Reset game input not accepted: there was a bug when the user inserted 'Yes' for resetting the game, the system did not recognize the 'Yes' correctly. This was fixed by using a try and except statement instead of an if statement.
* System clear: console was cleared at the wrong moment. By putting it before the guess_handling it now shows the result of the player's guess.

**Unsolved bugs**
As far as I could find there are no outstanding bugs.

## Deployment
**Heroku**
The project was deployed to Heroku using the following steps:
1. I pushed my final code via the terminal after finishing the project.
2. I created a new Heroku app
3. I set the buildbacks to 'Python' and 'NodeJS' in that order
4. I linked the Heroku app to the repository
5. Then I selected 'deploy'

## Credits
**Code**
* The structure of the class is based on the CodeInstitute scope example
* The code for the printing of the board is the CodeInstitute scope example

**Acknowledgements**
* I want to thank the tutors for guiding me 
* I thank my mentor for his review and feedback on my project
* I thank my fellow students for providing me with suggestions via Slack
* I want to CodeInstitute for the modules that made me capable of writing this code
---

Thank you!