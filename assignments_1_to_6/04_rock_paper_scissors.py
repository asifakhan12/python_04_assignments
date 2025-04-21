import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    user = input("Choose (rock, paper, or scissors): ").lower()
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)

    if user not in choices:
        print("❌ Invalid input. Please choose rock, paper, or scissors.")
        return

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("🤝 It's a tie!")
    elif is_win(user, computer):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

def is_win(player, opponent):
    # return True if player beats opponent
    return (
        (player == "rock" and opponent == "scissors") or
        (player == "scissors" and opponent == "paper") or
        (player == "paper" and opponent == "rock")
    )

def main():
    while True:
        play()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
