import random
# Possible choices for the game
choices = ["rock", "paper", "scissors"]
# Initialize the score for user and computer
User_score = 0
Computer_score = 0
Playing = True
while Playing:
  # Random choose the computer's from the list
    computer = random.choice(choices)
  # Initialize the user's choice to None before input
    User = None
    while User not in choices:
      # Ask the user for their choice and convert it to lowercase
        User = input("Enter a choice (rock, paper, scissors): ").lower()
      # If the user's input is not valid, print an error message
        if User not in choices:
            print("Invalid choice!, try again")
     # Display both the user's and the computer's choices     
    print(f"User: {User}")
    print(f"Computer: {computer}")

    # Check the result of the round
    if User == computer:
        print("It's a Tie!")
    elif User == "rock" and computer == "scissors":
        print("User wins")
        User_score += 1
    elif User == "paper" and computer == "rock":
        print("User wins")
        User_score += 1
    elif User == "scissors" and computer == "paper":
        print("User wins")
        User_score += 1
    else:
        print("Computer wins")
        Computer_score += 1
# Display the current scores of both the user and the computer
    print(f"User score: {User_score}")
    print(f"Computer score: {Computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if not play_again == 'yes':
        Playing = False
# Once the loop ends, thank the user for playing
print("Thanks for playing!")
