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
from Session_4.Exercise_2.python_template import python_template_setup
from Session_4.Exercise_3.random_user import random_user_request
from Session_5.Exercise_1.pokemon_database import pokemon_database_analysis
from Session_5.Exercise_2.automobile_class import automobile_class_demo
from Session_5.Exercise_3.automobile_children_classes import automobile_children_classes_demo
from Final_Project.student_directory import student_directory_app

def console():
  firstTime = True
  while True:
    if firstTime:
      make_header('EXERCISES LAUNCHER', 'Easily launch deliverable exercises.')
      firstTime = False
      print('\033[F\033[F\033[F')
      loader(1.2, 'blue')
      print('\n\nWhich exercise would you like to run?')
    else:
      time.sleep(1)
      print('Which exercise would you like to run now?')
      
    print('''
[11]  1.1 Hello World
[12]  1.2 Hello Name
[21]  2.1 Investment Calculator
[31]  3.1 Investment Calculator App
[32]  3.2 Primes 1 to 100u
[33]  3.3 Leap or Not
[411] 4.1.1 Primes in Range
[412] 4.1.2 Primes Checker
[413] 4.1.3 Leap Checker
[42]  4.2 Python Template
[43]  4.3 Random User API Access
[51]  5.1 Pokemon Data Analysis
[52]  5.2 Automobile Class
[53]  5.3 Automobile Children Classes
[61]  6.1 Final Project: Student Directory
[X]   Exit
    ''')
    option = input().lower()
    options = {
      '11': hello_world_function,
      '12': hello_name_function,
      '21': calculate_investment,
      '31': investment_app,
      '32': display_primes_1_to_100,
      '33': leap_or_not_function,
      '411': display_primes_in_range,
      '412': prime_checker_function,
      '413': leap_checker_function,
      '42': python_template_setup,
      '43': random_user_request,
      '51': pokemon_database_analysis,
      '52': automobile_class_demo,
      '53': automobile_children_classes_demo,
      '61': student_directory_app,
    }
    if option in options:
      options[option]()
    elif option == 'x':
      print('''            
Thank you for your time!

-----------------------
''')
      break
    else:
      print(colored("Oops! That's not a valid option. Try again...\n", 'red'))

if __name__ == '__main__':
  console()
  