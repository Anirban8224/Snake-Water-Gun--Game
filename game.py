import random

# Snake Water Gun Game
print("********** Welcome to the Snake,water,Gun Game **********\n")
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True
plyrwc = 0
compwc = 0
for i in range (1,4):
   print(f"*** Round {i} ***")
   print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
   randNo = random.randint(1, 3) 
   if randNo == 1:
      comp = 's'
   elif randNo == 2:
      comp = 'w'
   elif randNo == 3:
      comp = 'g'

   you = input("Your Turn: Snake(s) Water(w) or Gun(g)?\n")
   a = gameWin(comp, you)

   print(f"Computer chose: {comp}")
   print(f"You chose: {you}")

   if a == None:
      print("This round is a tie!\n")
   elif a:
      print("You Won this round!\n")
      plyrwc += 1
   else:
      print("You Lost this round!\n")
      compwc += 1
if plyrwc == compwc:
   print(f"The game is tie with a score of {plyrwc} - {compwc}")
elif plyrwc > compwc:
   print(f"You Won the game with a score of {plyrwc} - {compwc}")
else:
   print(f"Computer won the game with a score of {plyrwc} - {compwc}")
