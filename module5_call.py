from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    # Read N from the user
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            if n > 0:
                break
            else:
                print("N must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Read N numbers
    processor.read_numbers(n)

    # Read X from the user
    while True:
        try:
            x = int(input("Enter the number X to search for: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Search for X and output the result
    result = processor.search_number(x)
    if result == -1:
        print("-1")
    else:
        print(f"Number {x} found at index {result}.")

if __name__ == "__main__":
    main()
