import sys

def add_2_numbers(x, y):
    return x + y

if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>")
    sys.exit(1)

try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
except ValueError:
    print("Error: Both arguments must be numbers.")
    sys.exit(1)

result = add_2_numbers(x, y)
print(f"The sum of {x} and {y} is: {result}")
