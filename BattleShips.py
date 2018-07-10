# -*- coding: utf-8 -*-

# Used for random position of ships
from random import randint

board = []

# Create a table of 5 x 5 of "O"s
for x in range(5):
  board.append(["O"] * 5)

# Print them in an nice way
def print_board(board):
  for row in board:
    print((" ").join(row))

# For a random location of a ship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_row2 = random_row(board) + 1

ship_col = random_col(board)
ship_col2 = random_col(board) + 1

ships = [[ship_row, ship_col], [ship_row2, ship_col2]]

hit1 = False
hit2 = False
turn = 0

name = input("Hello! What is your name?")
print()
print(f"Hello there, {name}")
print("Welcome to Battleships!")
print("This is the Battle Board:")
print()
print_board(board)
print()
print("The rules are simple: ")
print("Try to hit my ship in less than 4 tries!")
print("It may sound easy, but you will find it pretty challenging over the time")

ans =  input("Ready to start? (Y/N)")
if(ans == 'Y' or ans == 'y'):
    print("Ok then! Let\'s go!")
elif(ans == 'N' or ans == 'n'):
        print("Alright! Start when you are ready")
        #break

# Check what happens next
while turn < 4:
  # Get the guess from the player
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  #if guess_row == ship_row1 and guess_col == ship_col1:
  if(guess_row == ship_row and guess_col == ship_col):
        print("Congratulations! You sunk my battleship!")
        hit1 = True
        if(hit1 == True):
            print("You have won the game!")
            break
  	# If the numbers are exactly like the random ones,
  	#	the ship is destroyed
  elif(guess_row not in range(0,5) or guess_row not in range(0,5)):
        	print("Oops, that's not even in the ocean.")
    	# Protects against going over the range of 5 by 5
  elif(board[guess_row][guess_col]) == "X":
        	print("You guessed that one already.")
    	# Don't guess twice the same place
  else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        	# Print (turn + 1) here!
        if(turn == 3):
          	print("Game Over")
          	ans = input("Want a rematch? (Y\\N)?")
          	if(ans == 'Y' or ans == 'y'):
            	  turn = 0
          	else:
                  print(f"Comeback anytime for a new game, {name}! :)")
                  break
        else:
          	print(f"Turn {turn + 1}")
          	turn += 1
          	print_board(board)