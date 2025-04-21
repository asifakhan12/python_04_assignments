#Problem Statement
"""Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height."""

MINIMUM_HEIGHT : int = 50 # arbitrary units :)

def main():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()