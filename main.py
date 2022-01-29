import random 

def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    #  Check for all possibilties when computer chose s
    elif comp == "s":
        if you =='w':
            return False
        elif you=='g':
            return True

    #  Check for all possibilties when computer chose w
    elif comp == 'w':
        if you== 'g':
            return False
        elif you == 's':
            return True

    #  Check for all possibilties when computer chose g
    elif comp =='g':
        if you =='s':
            return False
        elif you == 'w':
            return True

print("Comp Trun: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'g'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("Game Tied!🤨")
elif a:
    print(" WOW!!Tu jit gaya 🤑")
else:
    print("Better Luck Next Time☹")
    





