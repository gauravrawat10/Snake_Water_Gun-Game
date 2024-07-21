import random

def get_computer_choice():
    """Randomly choose between Snake, Water, Gun."""
    return random.choice(['Snake', 'Water', 'Gun'])

def get_user_choice():
    """Get user's choice."""
    user_choice = input("Enter your choice (Snake, Water, Gun): ").capitalize()
    while user_choice not in ['Snake', 'Water', 'Gun']:
        print("Invalid choice! Please choose either Snake, Water, or Gun.")
        user_choice = input("Enter your choice (Snake, Water, Gun): ").capitalize()
    return user_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner between user and computer."""
    if user_choice == computer_choice:
        return "tie"
    
    if ((user_choice == 'Snake' and computer_choice == 'Water') or 
        (user_choice == 'Water' and computer_choice == 'Gun') or 
        (user_choice == 'Gun' and computer_choice == 'Snake')):
        return "user"
    else:
        return "computer"

def play_game():
    """Play the Snake, Water, Gun game."""
    user_wins = 0
    computer_wins = 0
    ties = 0
    
    rounds = int(input("Enter the number of rounds you want to play: "))

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            print("You win this round!")
            user_wins += 1
        elif result == "computer":
            print("Computer wins this round!")
            computer_wins += 1
        else:
            print("This round is a tie!")
            ties += 1
        
        print()  # Print a newline for better readability
    
    print(f"Final Results after {rounds} rounds:")
    print(f"You won {user_wins} times.")
    print(f"Computer won {computer_wins} times.")
    print(f"There were {ties} ties.")
    
    if user_wins > computer_wins:
        print("Congratulations! You won the game.")
    elif computer_wins > user_wins:
        print("Computer won the game. Better luck next time!")
    else:
        print("The game is a tie.")

if __name__ == "__main__":
    play_game()
