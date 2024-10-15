import time
from termcolor import colored

#################################################
# Check if a number is prime.
#################################################
def is_prime(num):
  # Verify if the number has any divisor
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
      break
  # If it has no divisor, it is a prime number
  return True

#################################################
# Check if a year is a leap year.
#################################################
def is_leap_year(year: int) -> bool:
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

#################################################
# Ask for an input passing a question
# and optionally a variable type (default: int).
#################################################
def ask_input(question, var_type=int):
  while True: 
    try:
      print('\n' + question)
      return var_type(input())
    except ValueError:
      print(colored("Oooooops! That's not a valid number. Try again...\n", 'red'))

#################################################
# Loader in x seconds
#################################################
def loader(duration):
  print('''
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''', end='\r')
  for i in range(49):
    print('▓', end='', flush=True)
    interval = round(duration / 49, 2)
    time.sleep(interval)