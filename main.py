'''
1 for snake
-1 for water 
0 for gun
'''
# test

import random

computer = random.choice([1,-1,0])
youstr = input("Enter the choice: ").lower()
youdict = {"s":1,
           "w":-1,
           "g":0}
reverseddict = {1:"Snake",     
                -1:"Water",
                0:"Gun"}
# upto this you can get the choices of both user and computer.

you = youdict[youstr]
print(f"You chose {reverseddict[you]}\nComputer chose {reverseddict[computer]}")

if computer == you:
    print("Its a tie")
else:
    if computer == -1 and you == 1:
        print("You win!!")
    
    elif computer == -1 and you == 0:
        print("You lose!!")
    
    elif computer == 1 and you == -1:
        print("You lose!!")
    
    elif computer == 1 and you == 0:
        print("You win!!")
    
    elif computer == 0 and you == 1:
        print("You win!!")
    
    elif computer == 0 and you == 1:
        print("You lose!!")
    else:
        print("Something went wrong")
    
