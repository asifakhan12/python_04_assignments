# Problem #1: List Practice

def list_practice():
    # Create a list with fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Length of fruit_list:", len(fruit_list))

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print("Updated fruit_list:", fruit_list)


# Problem #2: Index Game Functions

def access_element(lst, index):
    if index >= 0 and index < len(lst):
        return lst[index]
    else:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    if index >= 0 and index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid slice range!"
    return lst[start:end]


# Problem #2: Interactive Game

def index_game():
    my_list = ['python', 'java', 'c++', 'javascript', 'go']

    while True:
        print("\nList Game Options:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated List:" if isinstance(result, list) else "Error:", result)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(my_list, start, end))

        elif choice == '4':
            print("Exiting game. Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")

        print("Current List:", my_list)


# Main function to run both parts

def main():
    print("----- Problem #1: List Practice -----")
    list_practice()

    print("\n----- Problem #2: Index Game -----")
    index_game()


if __name__ == "__main__":
    main()
