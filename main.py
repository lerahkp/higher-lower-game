from art import logo,vs
from game_data import data
import random
import replit
score=0
continue_game = True
print(logo)

fc1=''
fc2=''
d1=''
d2=''
n1= random.randint(0,50)
n2= random.randint(0,50)

if n1 == n2:
  n2 = random.randint(0,50)

def dictvalue1():
  d1 = (data[n1-1])
  global fc1
  fc1 = d1["follower_count"]
  print("Compare A: " + d1["name"]+", a "+ d1["description"]+", from "+ d1["country"])

def dictvalue2():
  d2=(data[n2-1])
  global fc2
  fc2 = d2["follower_count"]
  print("Against B: " + d2["name"]+", a "+ d2["description"]+", from "+ d2["country"])

def compare():
  global score
  global continue_game
  replit.clear()
  print(logo)
  if fc1 > fc2 and user_choice == 'a':
    score+=1
    print(f"You're right, current score: {score}.")
  elif fc2 > fc1 and user_choice == 'b':
    replit.clear()
    print(logo)
    score+=1
    print(f"You're right, current score: {score}.")
  else:
    replit.clear()
    print(logo)
    print(f"Sorry, that's wrong, final score: {score}.")
    continue_game=False

def next_value():
  global n1, n2
  global d1, d2
  if fc1 > fc2:
    n2 = random.randint(0,50)
  elif fc2>fc1:
    n1 = n2
    n2 = random.randint(0,50)

while continue_game:
  dictvalue1()
  print(vs)
  dictvalue2()
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  compare()
  next_value()
