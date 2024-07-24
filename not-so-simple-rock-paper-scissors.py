rock = "Rock"

paper = "Paper"

scissors = "Scissors"

#Write your code below this line 👇
import random

user_choice = input("Choose between \"Rock\", as 0, \"Paper\", as 1 or \"Scissors\", as 2\n")

def myrando():

    base1 = random.random()
    base2 = random.random()

    if base2 < base1:
        if base2 < base1 / 3 :
            choice = rock
        elif base2 < (base1 / 3) + (base1 / 3) :
            choice = paper
        else:
            choice = scissors
    elif base2 > base1:
        if base2 < base1 + (base1 / 3):
            choice = scissors
        elif base2 < base1 + (base1/3) + (base1/3) :
            choice = paper
        else:
            choice = rock
    else:
        base2 = random.random()
        if base2 < base1:
            if base2 < base1 / 3 :
                choice = rock
            elif base2 < (base1 / 3) + (base1 / 3) :
                choice = paper
            else:
                choice = scissors
        else:
            if base2 < base1 + (base1 / 3):
                choice = rock
            elif base2 < base1 + (base1/3) + (base1/3) :
                choice = paper
            else:
                choice = scissors


    return choice
choice_out = myrando()
print("\033c", end = "", flush=True)
print(f"You chose {user_choice}.")
print(f"Adversary chose: {choice_out}.")

result = user_choice + choice_out
if len(user_choice) == len(choice_out):
    print("It do be a draw.")
else:
    if len(result) == len(rock) + len(scissors) and result[0] == "R":
        print("You win.")
    elif len(result) == len(paper) + len(rock) and result[0] == "P":
        print("You win.")
    elif len(result) == len(scissors) + len(paper) and result[0] == "S":
        print("You win.")
    else:
        print("You lose.")
