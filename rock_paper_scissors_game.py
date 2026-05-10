import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:

    print("\n==== ROCK PAPER SCISSORS GAME ====")

    # User input
    user = input("Enter rock, paper, or scissors: ").lower()

    # Invalid input check
    if user not in choices:
        print("Invalid input! Try again.")
        continue

    # Computer choice
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    # Game logic
    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    # Score display
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    # Ask to continue
    again = input("Do you want to play again? (yes/no): ").lower()

    if again == "no":
        print("Game Over!")
        break

print("Thanks for playing!")
input("Press Enter to exit...")