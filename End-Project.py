import random

def get_user_choice():
   
    print("Choose one: Rock, Paper, or Scissors")
    user_input = input("Your choice: ").strip().lower()
    if user_input in ["rock", "paper", "scissors"]:
        return user_input
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

def get_computer_choice():
    
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
   
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