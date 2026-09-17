"""
Module: smaller-number.py

Purpose: Compare two numbers and return the smaller value.
         Returns "Equal" when both numbers are identical.

Usage:
    python smaller-number.py
    
    The script prompts the user to enter two numbers separated by a space,
    then prints which number is smaller (or if they are equal).
"""


def smaller_number(a, b):
    """
    Compare two numbers and return the smaller one.
    
    Args:
        a: First number to compare.
        b: Second number to compare.
        
    Returns:
        int/float: The smaller of the two numbers.
        str: "Equal" if both numbers are identical.
    """
    # Check if 'a' is less than 'b'
    if a < b:
        return a
    # Check if 'a' is greater than 'b'
    elif a > b:
        return b
    # Both numbers are the same value
    else:
        return "Equal"

# Main block: runs only when this script is executed directly
if __name__ == "__main__":
    # Read two numbers from user input, split by whitespace and convert to integers
    a, b = map(int, input("Enter two numbers: ").split())

    # Call the function and print the result
    print(smaller_number(a, b))