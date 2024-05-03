# Ah, yes. Rock, paper, scissors. A simple game with a simple objective, but using oh-so-many complicated strategies.
# Here lies my simple, yet powerful code, which shows how powerful simplicity can be.

import random

strategy_name = "random as first move, and then make move based on my previous input"

def move(my_history, their_history):
    
    # starting the random
    if len(my_history) == 0:
      my_move = random.choice(["r", "p", "s"])
        
    else:
    # the code if it isn't the first turn:
        # history for the cycle to COMMENCE
      prev_move = my_history[-1]
      my_move = ""
        # the simple cycle itself is below
        
      if prev_move == 'r':
          my_move = 's'
  
      elif prev_move == 'p':
          my_move = 'r'
  
      elif prev_move == 's':
          my_move = 'p'
          
          # filler section, but ig its a last resort
      else:
          my_move = random.choice(["r", "p", "s"])
          
  # return final move and pray to the universe
    return my_move
# its so beatiful (:
