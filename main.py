# Rules
# Rock wins against scissors.
# Paper wins against rock.
# Scissors win against paper.

import random
from art_work import rock, paper, scissors

game_end = False
while not game_end: 
  
  user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

  # User Input
  if user_input == 0:
    print(f"You chose Rock")
    print(rock) 
  elif user_input == 1:
    print(f"You chose Paper")
    print(paper)
  elif user_input == 2:
    print(f"You chose Scissors")
    print(scissors)
  else:
    print("Your choice is not a valid entry.")

  # Computer random choice
  computer_choice = random.randint(0, 2)
  if computer_choice == 0:
    print(f"Computer chose Rock")
    print(rock) 
  elif computer_choice == 1:
    print(f"Computer chose Paper")
    print(paper)  
  elif computer_choice == 2:
    print(f"Computer chose Scissors")
    print(scissors)

  # Result
  if user_input == computer_choice:
    print(f"It is a tie")
  elif user_input == 0 and computer_choice == 1:
    print(f"You lose")
  elif user_input == 0 and computer_choice == 2:
    print(f"You win!")
  elif user_input == 1 and computer_choice == 0:
    print(f"You win!")
  elif user_input == 1 and computer_choice == 2:
    print(f"You lose")
  elif user_input == 2 and computer_choice == 0:
    print(f"You lose")
  elif user_input == 2 and computer_choice == 1:
    print(f"You win!")
  else:
    print(f"You lose") 
  # option to restart the game.
  
  restart = input('Type "yes" if you want to play again -- otherwise type "no". \n')
  if restart == "no":
    game_end = True
    print("Goodbye")