import random

# Function to decide the winner
def get_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a Tie!"
    elif (choice1 == "rock" and choice2 == "scissor") or \
         (choice1 == "paper" and choice2 == "rock") or \
         (choice1 == "scissor" and choice2 == "paper"):
        return "Player 1 Wins!"
    else:
        return "Player 2 Wins!"

# User vs Computer
def user_vs_computer():
    user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissor"])
    print(f"Computer chose: {computer_choice}")
    print(get_winner(user_choice, computer_choice))

# User1 vs User2
def user_vs_user():
    user1_choice = input("User1, enter your choice (rock/paper/scissor): ").lower()
    user2_choice = input("User2, enter your choice (rock/paper/scissor): ").lower()
    print(get_winner(user1_choice, user2_choice))

# Main Game Menu
def main():
    while True:
        print("\nRock Paper Scissor Game")
        print("1. User vs Computer")
        print("2. User vs User")
        print("3. Exit")

        choice = input("Enter your option: ")

        if choice == "1":
            user_vs_computer()
        elif choice == "2":
            user_vs_user()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again!")

main()
