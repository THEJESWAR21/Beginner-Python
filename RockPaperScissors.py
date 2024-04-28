import random 

option = ["Rock","Paper","Scissors"]

user_choice = input("Your Choice (Rock, Paper or Scissors): ")
computer_choice = random.choice(option)

print("Your Choice:",user_choice)
print("Computer Choice:",computer_choice)

user = 0
computer = 0

if user_choice == computer_choice:
    print("DRAW!!!",end="")
    result="Draw"
elif user_choice == "Paper" and computer_choice == "Rock":
    print("YOU WIN!!!",end="")
    result="User_Wins"
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("YOU WIN!!",end="")
    result="User_Wins"
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("YOU WIN!!",end="")
    result="User_Wins"

else:
    print("COMPUTER WINS!")
    result=("Computer_Wins")

