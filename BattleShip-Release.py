"""
BattleShip Game
User VS Computer - Blast the enemy ship to Win.
Created By: Blackranger07
March 7, 2019
Changelog:
Version 1.1
-Added Ship location to board after a loss with the icon S.
-Imported os into program so that clear/cls function can be implemented.
-Imported sleep from time for loading effect when starting BattleShip.
-Added While loop
-Created function create_board
-Added Play Again functionality.
"""
# Imported Modules into program.
from random import randint
from time import sleep
import os

os.system("cls")

logo = """
                __/___
          _____/______|
  _______/_____\_______\_____
  \              < < <       |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Welcome To BattleShip!
A warship is on the horizon, destroy it
or perish. You have 5 attempts. Good luck cadet...
"""

explosion = """
     _.-^^---....,,--
 _--                  --_
<                        >)
|         BOOM!!!         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____
"""

death = """
**********************************************************************************
*   I've seen things you people wouldn't believe. Attack ships on fire off       *
*   the shoulder of Orion. I watched C-beams glitter in the dark near the        *
*Tannhauser Gate. All those moments will be lost in time... like tears in rain...*
*                             Time to die...                                     *
**********************************************************************************
"""

print(logo)
sleep(2)

def create_board():
    # Empty list created for our playing board.
    board = []
    # Columns and rows entered into board by the range()
    for x in range(5):
      board.append(["O"] * 5)
    return board

def print_board(board):
  print "The Ocean"
  print "~^-^~^-^~"
  for row in board:
    print " ".join(row)

# Random positions for Ship location
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

play_again = 'y'

# While and nested for loop started for Batteship Guesses and Updated board.
while (play_again == "Y" or play_again == "y"):
    os.system("cls")
    print(logo)
    board = create_board()
    print_board(board)
    print ""
    ship_row = random_row(board)
    ship_col = random_col(board)
    # The two lines below are for debugging purposes only. Ship location printed to screen.
    #print ship_row
    #print ship_col
    for turn in range(5):
        print ""
        print "Turn", turn + 1
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
        if guess_row == ship_row and guess_col == ship_col:
          os.system("cls")
          print(death)
          sleep(15)
          os.system("cls")
          print(explosion)
          print "Noooo! You sunk my battleship!"
          break
        else:
          if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            os.system("cls")
            print(logo)
            print "Oops, that's not even in the ocean."
            print ""
          elif(board[guess_row][guess_col] == "X"):
            os.system("cls")
            print(logo)
            print "You guessed that one already."
            print ""
            print board[guess_row][guess_col]
          else:
            os.system("cls")
            print(logo)
            print "You missed my battleship!"
            print ""
            board[guess_row][guess_col] = "X"
          print_board(board)
     # Turn must be -1 of the range so that Gameover will print after the final attempt if the answer is wrong.
          if turn == 4:
            os.system("cls")
            print(logo)
            print ""
            print "*=======================================================*"
            print "*Game Over! Your family will be notified of your death. *"
            print "*The ship (S) left its location Row [ %d ] and Col [ %d ].*" % (ship_row, ship_col)
            print "*=======================================================*"
            print ""
            board[ship_row][ship_col] = "S"
            print_board(board)
    print ""
    play_again = raw_input("Play Again? Y or N: ")
