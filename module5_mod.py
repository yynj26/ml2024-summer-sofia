class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        """Reads N numbers from the user and stores them."""
        for i in range(n):
            while True:
                try:
                    number = int(input(f"Enter number {i + 1}: "))
                    self.numbers.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

    def search_number(self, x):
        """Searches for the number X and returns its 1-based index or -1 if not found."""
        try:
            index = self.numbers.index(x)
            return index + 1  # Return 1-based index
        except ValueError:
            return -1


