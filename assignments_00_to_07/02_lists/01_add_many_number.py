#Problem Statement
"""Write a function that takes a list of numbers and returns the sum of those numbers."""

def add_many_numbers(numbers):
    num:int=0
    for number in numbers:
        num+=number
    return num

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(f"sum_of_numbers: {sum_of_numbers}")  # Print out the sum above
    

if __name__ == '__main__':
    main()