import random

# Likelihood of stopping early
DONE_LIKELIHOOD = 0 # You can change this to test different behaviors

# Seed the random number generator for consistent results during testing
random.seed(1)

def chaotic_counting():
    """
    Prints numbers from 1 to 10 unless 'done()' randomly returns True.
    """
    for i in range(1, 11):
        if done():
            return  # Stop counting early
        print(i)

def done():
    """
    Returns True with a probability of DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()
