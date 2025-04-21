#Problem Statement
"""Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!"""

def main()->None:
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print("The " + adjective + " " + noun + " decided to " + verb + " through the forest!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()