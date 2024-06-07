def fibonacci_generator(n):
    """
    Generator function to yield the Fibonacci series up to n terms.
    
    Parameters:
    n (int): The number of terms to generate in the Fibonacci series.
    
    Yields:
    int: The next number in the Fibonacci series.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def main():
    """
    Main function to interact with the user and print the Fibonacci series.
    """
    print("Welcome to the Fibonacci Generator!")
    try:
        n = int(input("Enter the number of terms you want in the Fibonacci series: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        print(f"Fibonacci series up to {n} terms:")
        for number in fibonacci_generator(n):
            print(number, end=" ")
        print()
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
