#Problem Statement
"""Print 10 random numbers in the range 1 to 100."""


import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)
        print(num, end=' ')

if __name__ == '__main__':
    main()