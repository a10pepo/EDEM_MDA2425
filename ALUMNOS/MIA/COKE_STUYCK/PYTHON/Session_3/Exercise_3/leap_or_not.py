import time
from functions import is_leap_year, make_header, ask_input
from termcolor import colored

def leap_or_not_function():
  make_header('LEAP YEAR OR NOT?', 'Given a list of years, checks if each one is a leap year or not.', bg_color='yellow')
  
  year_from = ask_input('Which is the first year of the range you want to check?')
  year_until = ask_input('Which is the last year of the range you want to check?')
  
  year_list = list(range(year_from, year_until + 1))

  print('')
  # Identify from a list of years if they are leap years.
  for year in year_list:
    time.sleep(0.3)
    print(colored(f'{year}: It is a leap year', 'green') if is_leap_year(year) else colored(f'{year}: It is not a leap year', 'red'))

  print('''
-----------------------
''')
  
if __name__ == '__main__':
  leap_or_not_function()
