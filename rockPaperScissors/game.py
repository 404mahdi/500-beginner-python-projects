import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()
    return choice

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "You win!"
    
    return "Computer wins!"

def play_game():
    print("🎮 Rock Paper Scissors Game")

    user = get_user_choice()
    computer = get_computer_choice()

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    result = decide_winner(user, computer)
    print(result)

if __name__ == "__main__":
    play_game()
