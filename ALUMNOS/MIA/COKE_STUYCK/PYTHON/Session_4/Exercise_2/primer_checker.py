import time
from termcolor import colored

from functions import is_prime, ask_input
# Check if a number is prime.
def prime_checker():
  print('''
▄▄ IS IT PRIME? ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                               █
█  Checks if a number is prime.                 █ 
█                                               █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')
  number = ask_input('Which number do you want to check?')

  if is_prime(number):
    print(colored(f'\n{number} is a prime number', 'green'))
  else:
    print(colored(f'\n{number} is not a prime number', 'red'))

  print("""                    
THAT'S ALL!
""")

# Call function to display prime numbers from 1 to 100
prime_checker()