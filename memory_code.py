import random
import time

print("Hello, and welcome to this memory game. The game gets faster the further on you go. A letter (A/B/C/D) will be displayed, and you will be asked to remember it and tell it back. \n\n")
time.sleep(3)
options = ["a", "b", "c", "d"]
#list of possible options
setPick = []
#the list that will store the randomly chosen item

for i in range(50):
    setPick.append(options[random.randint(0, 3)])
    print("Your letter is:", setPick[i], "____", end="\r")

    if i != 0:
        time.sleep(1 / int(i) * 3)
        #^ by making it a reciprocal, it goes faster the bigger i gets (the further into the program you go)
    else:
        time.sleep(2)
    guess = input("What was the Letter you just saw??? ")
    if guess == setPick[i]:
        continue
    elif guess != setPick[i]:
        break

print("Game Over")
print("This is a list of all letters you got through:", setPick)
print("Not including the final one you got wrong, you got: " + str((len(setPick) - 1)),"correct!! This means the final question you answered took you 3/" + str(int(len(setPick)) - 1) + " seconds to read the letter!")
