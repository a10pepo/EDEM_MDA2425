# Console application that calculates the results of an investment.
# The application should ask the user for:
#   The amount of investment (number)
#   The annual interest rate (%)
#   The number of years the investment will be held (number)
# The program should calculate and display:
#   The amount of the investment after the given period of time
from termcolor import colored

from functions import ask_input, loader, make_header

def calculate_investment():
  make_header('INVESTMENT CALCULATOR', 'Calculates the results of an investment.', bg_color='green')
  print(f'''
Hello!

Welcome to the investment calculator.''', end='')

  initial_investment = ask_input('''
-----------------------

How much would you like to invest?''')
  annual_interest = ask_input('What is the annual interest rate? (%)', float)
  years = ask_input('For how many years would you like to keep the investment?')
  
  result =  round(initial_investment * (1 + annual_interest / 100) ** years, 2)
  interest = round(result - initial_investment, 2)
  years_literal = 'year' if years == 1 else 'years'

  loader(1)

  print(f'''

After {years} {years_literal} you'll earn''')
  print(colored(interest, 'green', attrs=['bold']), end='')
  print(''' in interest.

-----------------------
''')

if __name__ == '__main__':
  calculate_investment()