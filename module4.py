def main():
    N = int(input("enter a positive input N: "))
    if N<= 0:
        print(" N must be a postive number")
        return 
    
    numbers = []
    for i in range(N):
        number = int(input(f"Enter number {i+1}: "))
        numbers.append(number)

    # Ask the user for input X (integer)
    X = int(input("Enter an integer X: "))

    # Check if X is among the N numbers and output the result
    if X in numbers:
        print(numbers.index(X) + 1)  # +1 to convert from 0-based to 1-based index
    else:
        print("-1")

if __name__ == "__main__":
    main()