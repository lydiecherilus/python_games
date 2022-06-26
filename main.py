import random
import os
from data import data
from art_work import art, vs


def clear_screen():
   """clear the screen for the next round"""
    # check if the operating system is Mac and Linux or Windows
   if os.name == "nt":
      os.system("cls")
   else:
      os.system("clear")


def answer_check(guess, A, B):
  """Checks who has more followers against user's guess""" 
  if A > B:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(art)
  score = 0
  is_game_end = True
  category_A = random.choice(data)
  category_B = random.choice(data)

  while is_game_end:
    category_A = category_B
    category_B = random.choice(data)

    # if the categories generated are the same, choose a different category_B
    while category_A == category_B:
      category_B = random.choice(data)

    print(f'Compare A: {category_A["name"]}, a {category_A["description"]}, from {category_A["country"]}')
    print(vs)
    print(f'Against B: {category_B["name"]}, a {category_B["description"]}, from {category_B["country"]}')
    
    guess = input("Who has more Instagram followers in millions? Type 'A' or 'B': ").lower()
    category_A_followers = category_A["follower_count"]
    category_B_followers = category_B["follower_count"]
    check_correct_answer = answer_check(guess, category_A_followers, category_B_followers)

    clear_screen()
    print(art)
    if check_correct_answer:
      score += 1
      print(f"You're right! Your current score is: {score}.")
    else:
      is_game_end = False
      print(f"Sorry, that's wrong. Your final score is: {score}")
      restart = input('Type "yes" if you want to guess another number -- otherwise type "no". \n')
      if restart == "no":
          print("Goodbye")
          return
      elif restart == "yes":
        print(art)
        return game()

game()
