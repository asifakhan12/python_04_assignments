def main():
    curr_value = int(input("Enter a starting number: "))
    
    while curr_value <= 100:
        print(curr_value)
        curr_value = curr_value * 2

# Required to call main()
if __name__ == '__main__':
    main()
