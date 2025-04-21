#Problem Statement
"""Ask the user for a number and print its square (the product of the number times itself)."""


def main():
    num: float = float(input("Type a number to see its square: ")) # Make sure to cast the input to a float so we can do math with it!
    print(str(num) + " squared is " + str(num ** 2)) # num * num is equivalent to num ** 2. The ** operator raises something to a power!

if __name__ == '__main__':
    main()
