import random

def get_user_choice():
    """Get the user's choice (rock, paper, or scissors)"""
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ('rock', 'paper', 'scissors'):
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Generate the computer's choice (rock, paper, or scissors)"""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game"""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a single round of the game"""
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

def main():
    """Main function to start the game"""
    play_again = 'yes'
    while play_again.lower() == 'yes':
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")

if __name__ == "__main__":
    main()
