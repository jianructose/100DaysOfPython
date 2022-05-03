from art import logo, vs
from game_data import data
import random
from replit import clear

def get_data():
  elem = random.choice(data)
  return elem

def parse_data(one_elem):
  # elem1= random.choice(data)
  parsed = f"{one_elem['name']}, a {one_elem['description']}, from {one_elem['country']}."
  return parsed

def compare(name1, name2):
  if name1['follower_count'] > name2['follower_count']:
    higher = name1
  else:
    higher = name2
  return higher
  

def play():
  print(logo)
  score = 0
  end_game = False
  na = get_data()
  nb = get_data()
  if na == nb:
    nb = get_data()
  while not end_game:
    na = nb
    nb = get_data()
    print(f"Compare A: {parse_data(na)}")
    print(vs)
    print(f"Against B: {parse_data(nb)}")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess == 'A':
      guess = na
    else:
      guess = nb
    clear()
  
    if guess == compare(na, nb):
      score +=1
      print(f"You are right! The current score is {score}")
    else:
      print(f"Unfortunately no. Your final score is {score}")
      # if input("Do you want to restart the game? 'y' or 'no'").lower() == 'y':
      #   end_game=False
      # else:
      end_game=True
  


play()