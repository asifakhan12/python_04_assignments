import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for i in range(10):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end=' ')

if __name__ == '__main__':
    main()
