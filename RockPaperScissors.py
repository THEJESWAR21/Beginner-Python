import random

choices = ["Rock","Paper","Scissors"]

p1 = input("Pick an option (Rock, Paper, Scissors): ")
p2 = random.choice(choices)


while True:
    if p1 == "Rock":
        if p2 == choices[0]:
            print("Draw",end="")
            result="Draw"
        elif p2 == choices[1]:
            print("AI Wins!!",end="")
            result="AI"
        elif p2 == choices[2]:
            print("User Wins!!")
            result="User"
    else:
        print("Didn't code it yet")
        continue


