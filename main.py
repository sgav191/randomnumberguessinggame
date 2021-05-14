import time
import random

print ("Welcome to the...")
time.sleep(1)
print ("RANDOM")
time.sleep(1)
print ("NUMBER")
time.sleep(1)
print ("GUESSING GAME!!!!")
time.sleep(1)
name = input ("Enter your name to continue: ")
print (f"Welcome to the game {name}!")
time.sleep(0.5)
print ("Entering game....")
time.sleep(5)
level = int(input ("CHOOSE YOUR LEVEL: "))

while level != 1 and level != 2 and level != 3:
  print ("You can only enter a value of 1,2, or 3. Please try again.")
  time.sleep (1)
  level = int(input ("CHOOSE YOUR LEVEL: "))

random_number = 0

if level == 1:
  random_number = random.randint(1,10)
  print ("Welcome to level 1!")
  time.sleep (1.5)
  print ("Please enter a number between 1 and 10.")
elif level == 2:
  random_number = random.randint(1,20)
  print ("Welcome to level 2!")
  print ("Please enter a number between 1 and 20.")
else:
  random_number = random.randint(1,30)
  print ("Welcome to level 3!")
  print ("Please enter a number between 1 and 30.")

userguess = int(input(">> "))
attempts = 1

while userguess != random_number:
  if userguess > random_number:
    print (f"Go lower {name}! Please try again.")
  else:
    print (f"Go higher {name}! Please try again")
  userguess = int(input(">> "))
  attempts = attempts+1

print (f"CONGRATULATIONS {name.upper()}!!!!!")
time.sleep(1)

if attempts > 5:
  print (f"And it only took you {attempts} attempts!")
else:
  print (f"But it did take {attempts} attempts.")