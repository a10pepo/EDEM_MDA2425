# Runs deliverable exercises effortlessly.

import time
from termcolor import colored
from functions import *
from Session_1.Exercise_1.hello_world import hello_world_function
from Session_1.Exercise_2.hello_name import hello_name_function
from Session_2.Exercise_1.investment_calculator import calculate_investment
from Session_3.Exercise_1.investment_calculator_app import investment_app
from Session_3.Exercise_2.primes_1_to_100 import display_primes_1_to_100
from Session_3.Exercise_3.leap_or_not import leap_or_not_function
from Session_4.Exercise_1.primes_in_range import display_primes_in_range
from Session_4.Exercise_1.primer_checker import prime_checker_function
from Session_4.Exercise_1.leap_checker import leap_checker_function


def console():
  firstTime = True
  while True:
    if firstTime:
      make_header('EXERCISES LAUNCHER', 'Easily launch deliverable exercises.')
      firstTime = False
      print('\nWhich exercise would you like to run?')
    else:
      time.sleep(1)
      print('Which exercise would you like to run now?')

    print('''
[11]  1.1 Hello World
[12]  1.2 Hello Name
[21]  2.1 Investment Calculator
[31]  3.1 Investment Calculator App
[32]  3.2 Primes 1 to 100
[33]  3.3 Leap or Not
[411] 4.1.1 Primes in Range
[412] 4.1.2 Primes Checker
[413] 4.1.3 Leap Checker
[42]  4.2 Python Template
[43]  4.3 Random User API Access
[51]  5.1 Pokemon Data Analysis
[52]  5.2 Automobile Class
[53]  5.3 Automobile Children Classes
[X]   Exit
    ''')
    option = input().lower()
    if option == '11':
      hello_world_function()
    elif option == '12':
      hello_name_function()
    elif option == '21':
      calculate_investment()
    elif option == '31':
      investment_app()
    elif option == '32':
      display_primes_1_to_100()
    elif option == '33':
      leap_or_not_function()
    elif option == '411':
      display_primes_in_range()
    elif option == '412':
      prime_checker_function()
    elif option == '413':
      leap_checker_function()
    elif option == 'x':
      print('''            
Thank you for your time!

-----------------------
''')
      break
    else:
      print(colored("Oops! That's not a valid option. Try again...\n", 'red'))

console()