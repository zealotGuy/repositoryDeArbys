# tic tac toe is a very fun game to play, so I made it using a simple python concept: 2d arrays
# basically you make 3 arrays(represents the 3 rows/columns in game) and use if statements to put where X and O goes

import time
# not me failing to use time function :\

board = [
  ["", "", ""],
  ["", "", ""],
  ["", "", ""] 
]

for row in board:
  print(row)
time.sleep(0.3)
print("Well hello there.")
time.sleep(0.5)
print("It looks like you have been challenged to a game of: TIC TAC TOE.")
time.sleep(0.8)
print("The rules are simple... You must choose a slot from the board.")
time.sleep(0.8)
print("KEYWORDS: topright, topmiddle, topleft, middleleft, center, middleright, bottomleft, bottommiddle, bottomright")
time.sleep(1.5)
print("Good luck, you may need it.")

player1 = "X"
player2 = "O"
current_player = player1

while True:
  print(f"Where would you like to place your {current_player} ?")
  choice = input()
  if choice == "topright" and board[0][2] == "":
    board[0][2] = current_player
  elif choice == "topmiddle" and board[0][1] == "":
    board[0][1] = current_player
  elif choice == "topleft" and board[0][0] == "":
    board[0][0] = current_player
  elif choice == "middleleft" and board[1][0] == "":
    board[1][0] = current_player
  elif choice == "center" and board[1][1] == "":
    board[1][1] = current_player
  elif choice == "middleright" and board[1][2] == "":
    board[1][2] = current_player
  elif choice == "bottomleft" and board[2][0] == "":
    board[2][0] = current_player
  elif choice == "bottommiddle" and board[2][1] == "":
    board[2][1] = current_player
  elif choice == "bottomright" and board[2][2] == "":
    board[2][2] = current_player
  else:
    print("That is not a valid input.")
    continue
  for row in board:
    print(row)
  if current_player == player1:
    current_player = player2
  else:
    current_player = player1

# voila its indestructible(kinda) (:
