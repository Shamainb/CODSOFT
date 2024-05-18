import random

def play_rps():
    """Play a single round of Rock, Paper, Scissors game."""

    user_choices = {"rock": 0, "paper": 1, "scissors": 2}
    computer_choices = {0: "rock", 1: "paper", 2: "scissors"}

# Get user's choice and validate
    user_choice = input("Enter your choice: 0 rock, 1 paper, or 2 scissors: ")

    while user_choice not in user_choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        # Get computer's choice randomly
    computer_choice = random.randint(0, 2)
    print("Computer chose:", computer_choices[computer_choice])

    # Convert user's choice to a numeric value
    user_choice_value = user_choices[user_choice]

    # Determine the winner
    if user_choice_value == computer_choice:
        print("It's a tie!")
    elif (user_choice_value + 1) % 3 == computer_choice:
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    play_again = True
    while play_again:
        play_rps()
        play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"
