import random

def guess_the_number():
    print("🎲 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} tries. The number was {secret_number}.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
