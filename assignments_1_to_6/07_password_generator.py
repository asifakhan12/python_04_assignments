import random
import string

def generate_password(length):
    # All characters we want to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        password_length = int(input("How long should each password be? "))

        print("\nHere are your generated passwords:\n")
        for i in range(num_passwords):
            print(f"{i+1}: {generate_password(password_length)}")
    except ValueError:
        print("❗ Please enter valid numbers.")

if __name__ == "__main__":
    main()
