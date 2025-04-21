import random
def main():
    random_guess=random.randint(0,99)
    while True:
        user_guess = int(input("Enter a guess between 0 and 99: "))
        if user_guess>random_guess:
            print("Your guess is too high")
        elif user_guess<random_guess:
            print("Your guess is too low")
        else :
            print(f"Congrats! The number was: {random_guess}")
            break


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()