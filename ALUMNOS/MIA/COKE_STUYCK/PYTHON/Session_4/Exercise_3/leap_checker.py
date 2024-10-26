import time
from termcolor import colored
from datetime import datetime

from functions import is_leap_year, ask_input


# Checks if a year is a leap year.
def leap_checker():
  print('''
▄▄ IS IT A LEAP YEAR? ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                               █
█  Checks if a year is a leap year or not       █
█                                               █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
  current_year = datetime.now().year

  input_year = ask_input('Which year do you want to check?')

  if is_leap_year(input_year):
    if input_year > current_year:
      print(colored(f'\n{input_year} will be a leap year', 'green'))
    if input_year < current_year:
      print(colored(f'\n{input_year} was a leap year', 'green'))  
    else:
      print(colored(f'\n{input_year} is a leap year', 'green'))
  else:
    if input_year > current_year:
      print(colored(f"\n{input_year} won't be a leap year", 'red'))
    if input_year < current_year:
      print(colored(f'\n{input_year} was not a leap year', 'red'))  
    else:
      print(colored(f'\n{input_year} is not a leap year', 'red'))

  print("""                    
THAT'S ALL!
""")

# Call function to display prime numbers from 1 to 100
leap_checker()