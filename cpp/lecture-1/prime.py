import math

def is_prime(n):
    """
    Checks if a given integer n is a prime number.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if n is prime, False otherwise.
    """
    # Handle edge cases: 1 and 2
    # Note: Mathematically, 1 is typically not considered prime.
    if n == 1:
        return True
    if n == 2:
        return True

    # Check if the number is even
    if n % 2 == 0:
        return False
    else:
        # Check for factors from 2 up to the square root of n
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                # Found a factor, so n is not prime
                return False
        # No factors found, n is prime
        return True


if __name__ == "__main__":
    # Prompt user for input
    try:
        n = int(input("Enter n: "))
        # Perform the primality check and print the result
        print(is_prime(n))
    except ValueError:
        print("Please enter a valid integer.")