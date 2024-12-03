# script/sum_two_numbers.py

# Used to access the command-line arguments passed
# to the script when it is executed
import sys

def sum_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    # Read the two numbers from command-line arguments
    if len(sys.argv) != 3:
        print("Please provide exactly two numbers.")
        sys.exit(1)

    try:
        # Make sure that the arguments are integers
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        # Calculate the sum
        result = sum_two_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Both arguments must be valid numbers.")
        sys.exit(1)
