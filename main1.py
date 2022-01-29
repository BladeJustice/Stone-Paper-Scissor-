import random
from playsound import playsound 


 
def gameWIn(comp, you):
    if comp == you:
        return None

    elif comp == 's':
       if you == 'c':   
        return False
       elif you == 'p':
           return True

    elif comp == 'p':
       if you == 's':   
        return False
       elif you == 'c':
           return True

    elif comp == 'c':
       if you == 'p':   
        return False
       elif you == 's':
           return True

print("comp turn stone(s) paper(p) scissor(c)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp  = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'c'

you = (input("Teri Bari stone(s) paper(p) scissor(c)?\n"))
a = gameWIn(comp ,you)

print(f"Computer Chose {comp}")
print(f"You  Chose {you}")

if a == None:
    print("Game Tied😑")
    playsound('G:\\python.code\\[Python Project-1 Snake Water Gun GAME]\\z.mp3')
 

elif a == True:
    print("You WIN🤑")
    playsound('G:\\python.code\\[Python Project-1 Snake Water Gun GAME]\\YouWin.mp3')
 

else:
    print("You Lose🤕")
    playsound('G:\\python.code\\[Python Project-1 Snake Water Gun GAME]\\Wah.mp3')
 





  