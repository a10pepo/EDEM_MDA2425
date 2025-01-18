import time
from termcolor import colored

from functions import is_prime, ask_input, make_header
# Check if a number is prime.
def prime_checker_function():
  make_header('IS IT PRIME?', 'Checks if a number is prime.', bg_color='magenta')

  number = ask_input('Which number do you want to check?')

  if is_prime(number):
    time.sleep(1.5)
    print(colored(f'\n{number} is a prime number', 'green'))
  else:
    time.sleep(0.5)
    print(colored(f'\n{number} is not a prime number', 'red'))

  print('''
-----------------------
''')

# Call function to display prime numbers from 1 to 100
if __name__ == '__main__':
  prime_checker_function()