import random 

option = ["Rock","Paper","Scissors"]

# Scores
user = 0
computer = 0

while True:

    # Inputs
    user_choice = input("Your Choice (Rock, Paper or Scissors): ")
    computer_choice = random.choice(option)

    # Display Choices
    print("Your Choice:",user_choice)
    print("Computer Choice:",computer_choice)

    # Draw
    if user_choice == computer_choice:
        print("DRAW!!!")
        result="Draw"

    # Choices that makes the user win
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("YOU WIN!!!")
        result="User_Wins"
        user = user + 1
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("YOU WIN!!")
        result="User_Wins"
        user = user + 1
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("YOU WIN!!",)
        result="User_Wins"
        user = user + 1

    else:
        print("COMPUTER WINS!")
        result=("Computer_Wins")
        computer = computer + 1
        
    if user < computer:
        print("Your Points", user) 
        print("Computer's Points", computer)
        print("COMPUTER WINS!")
    elif user == computer:
        print("Your Points", user)
        print("Computer's Points", computer)
        print("DRAW!!", )
    else:
        print("Your Points", user,)
        print("Computer's Points", computer)
        print("YOU WINS!") 
    
    if user == 3 or computer == 3:
        break
