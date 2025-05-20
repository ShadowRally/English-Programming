import random

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

WIN_RULES = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

def get_user_choice():
    print(f"Choose one: {', '.join(CHOICES).title()}")
    user_input = input("Your choice: ").strip().lower()
    if user_input in CHOICES:
        return user_input
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif computer_choice in WIN_RULES[user_choice]:
        return "win"
    else:
        return "lose"

def print_result(user_choice, computer_choice, result):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

def play_game():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    rounds = input("How many rounds would you like to play? (default 3): ").strip()
    try:
        rounds = int(rounds)
        if rounds < 1:
            rounds = 3
    except ValueError:
        rounds = 3
    print(f"You will play {rounds} rounds.")

    score = {"win": 0, "lose": 0, "tie": 0}

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num} of {rounds}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)
        score[result] += 1

    print("\nGame Over! Here are your results:")
    print(f"Wins: {score['win']}")
    print(f"Losses: {score['lose']}")
    print(f"Ties: {score['tie']}")

    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            play_game()
            break
        elif play_again == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()
