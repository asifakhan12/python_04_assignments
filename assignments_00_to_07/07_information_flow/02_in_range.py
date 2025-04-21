def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high


def main():
    # User se input lena
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    # in_range function ko call karna aur result print karna
    if in_range(n, low, high):
        print(f"{n} is in the range from {low} to {high}.")
    else:
        print(f"{n} is NOT in the range from {low} to {high}.")


# Program start yahan se hota hai
if __name__ == "__main__":
    main()
