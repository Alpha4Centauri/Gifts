import time
import os

def clear(): 
  os.system('clear') 


print("""|-| /-\ |~ |~ \|/ 
|\| . `|` |-| |`-__ |`/_ ' \~__ 
|-/ /-\ \|/ ! """)

time_limit = 10

while time_limit > 0:
  m, s = divmod(time_limit, 60)
  h, m = divmod(m, 60)
  time_Left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
  print(str(time_Left) + "\r", end="")
  time.sleep(1)
  time_limit -= 1

if time_limit == 0:
  a = input("Did you get it? ")
if a.lower() == "yes":
  b = input("What's the answer? ")
  if b == "Happy Mother's Day!":
    print("You got it, the answer is Happy Mother's Day!")
if a.lower() == "no":
  print("I've given you one hint, I'll now give you another")
  time.sleep(5)
  clear()

  print("What greeting happens every 40% through May?")

  time_limit = 7

  while time_limit > 0:
    m, s = divmod(time_limit, 60)
    h, m = divmod(m, 60)
    time_Left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    print(time_Left + "\r", end="")
    time.sleep(1)
    time_limit -= 1

  if time_limit == 0:
    a = input("Did you get it? ")

if a.lower() == "yes":
  b = input("What's the answer? ")
  if b == "Happy Mother's Day!":
    print("You got it, the answer is Happy Mother's Day!")

if a.lower() == "no":
  print("I've given you a second hint, now I'll give you a third one")
  time.sleep(5)
  clear()

  print("How did I greet you this morning?")

  time_limit = 5

  while time_limit > 0:
    m, s = divmod(time_limit, 60)
    h, m = divmod(m, 60)
    time_Left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    print(time_Left + "\r", end="")
    time.sleep(1)
    time_limit -= 1

  if time_limit == 0:
    a = input("Did you get it? ")
if a.lower() == "yes":
  b = input("What's the answer? ")
  if b == "Happy Mother's Day!":
    print("You got it, the answer is Happy Mother's Day!")
if a.lower() == "no":
  print("I've given you two hints, I'll now give you a third one")
  time.sleep(5)
  clear()

  print("""
        |   |      /\      ----    ----  \      /
        |   |     /  \     |  |    |  |   \    /
        |   |    /    \    |---    |---     \ /
        |---|   /------\   |       |         | 
        |   |  /        \  |       |         |  
        |   | /          \ |       |         |


                   ______   _____   |   |   ____   ___          ____
        |\     /| |      |    |     |   |  |      |   |  |      \  
        | \   / | |      |    |     |---|  |____  | __|          |
        |  \ /  | |      |    |     |   |  |      | \           /
        |       | |______|    |     |   |  |____  |  \      ___/




        |----   /\      \    /         |
        |   /  /  \      \  /          |
        |  /  /----\       |           | 
        | /  /      \      |          _ _
        |/  /        \     |         |___|
  """)

  print("What does this read?")

  time_limit = 4

  while time_limit > 0:
    m, s = divmod(time_limit, 60)
    h, m = divmod(m, 60)
    time_Left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    print(time_Left + "\r", end="")
    time.sleep(1)
    time_limit -= 1

  if time_limit == 0:
    a = input("Did you get it? ")
    if a.lower() == "yes":
      b = input("What's the answer? ")
      if b == "Happy Mother's Day!":
        print("You got it, the answer is Happy Mother's Day!")
    elif a.lower() == "no":
      print("If you haven't gotten it by now, the answer is Happy Mother's Day!")
      time.sleep(5)