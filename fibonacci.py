def fibonacci(n):
    a, b = 0, 1  # Initialize the first two terms
    for _ in range(n):
        print(a, end=" ")  # Print the current term
        a, b = b, a + b  # Update for the next term

# Example usage:
terms = int(input("Enter the number of terms: "))
fibonacci(terms)
