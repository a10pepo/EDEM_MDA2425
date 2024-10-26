# Based on console application that calculates the results of an investment.
# The application should incorporate a feature:
#   A menu with the following options: 
#     [1] Calculate an investment
#     [X] Exit 
#       In this case the program should display a goodbye message and exit

import time
from termcolor import colored
from functions import make_header
from Session_2.Exercise_1.investment_calculator import calculate_investment

def investment_app():
  firstTime = True
  while True:
    if firstTime:
      print(f'''
What would you like to do?
''')
      firstTime = False
    else:
      time.sleep(1)
      print('What do you want to do now?')
    
    print('''      
[1] Calculate an investment
[X] Exit
    ''')
    option = input().lower()
    if option == '1':
      calculate_investment()
    elif option == 'x':
      print('''            
Best of luck on your investments!

-----------------------
''')
      break
    else:
      print(colored("Oops! That's not a valid option. Try again...\n", 'red'))

if __name__ == '__main__':
  investment_app()