import random 

# Lists
option = ["Rock","Paper","Scissors"]

# Scores
user = 0
computer = 0

while True:

    # Inputs
    print("")
    user_choice = input("Your Choice (Rock, Paper or Scissors): ")

    ## Randomly Picks an option from the list
    computer_choice = random.choice(option)
    print("")


    # Display Choices
    print("================= Moves =====================")
    print("Your Choice:",user_choice)
    print("Computer Choice:",computer_choice)

    # Draw
    if user_choice == computer_choice:
        print("============= Results ================")
        print("DRAW!!!!")
        
    # Choices that makes the user win
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("============= Results ================")
        print("You WINNNNN!!!!")
        user = user + 1
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("============= Results ================")
        print("You WINNNNN!!!!")
        user = user + 1
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("============= Results ================")
        print("You WINNNNN!!!!")
        user = user + 1
    
    # Choices
    else:
        print("")
        print("============= Results ================")
        print("COMPUTER WINNNN!!!")
        # Score Increments By 1
        computer = computer + 1

    ## Score Display
    print("========== Scores ================")
    print("Your Points:", user) 
    print("Computer's Points:", computer)

# Conditions for Score Comparisons
    if user == 3 or computer == 3:
    # Computer Wins
        if user < computer:
            print("")
            print("COMPUTER WINS THE GAME")
        elif user == computer:
        # Draw
            print("")
            print("THE GAME END IN A DRAW")
        else:
    # Player Wins
            print("")
            print("YOU WON THE GAME")


# Stopping the loop after the max score is reached
    if user == 3 or computer == 3:
    # The Game ends when the player or the computer reaches the score of 3
        break