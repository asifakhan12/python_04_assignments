#Problem Statement
"""There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs."""

def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0

    for fruit_name in fruits:
        user_input = input("How many (" + fruit_name + ") do you want to buy?: ")

        if user_input == "":
            break  # if user presses Enter with no input, stop asking

        amount_bought = int(user_input)
        price = fruits[fruit_name]
        total_cost += price * amount_bought

    print("Your total is $" + str(total_cost))



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()