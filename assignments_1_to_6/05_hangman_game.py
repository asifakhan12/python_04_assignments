import random

# List of words to choose from
words = ['python', 'hangman', 'challenge', 'kylie', 'programming', 'developer', 'keyboard', 'function']

# Function to pick a random word
def get_word():
    return random.choice(words).upper()

# Display the game
def display(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game function
def play():
    word = get_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_tries = 6

    print("🎯 Welcome to Hangman!")
    print("_ " * len(word))

    while wrong_guesses < max_tries:
        guess = input("\nGuess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! You have {max_tries - wrong_guesses} tries left.")

        current_display = display(word, guessed_letters)
        print("\n" + current_display)

        if "_" not in current_display:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Out of tries. The word was:", word)

# Run the game
if __name__ == "__main__":
    play()
