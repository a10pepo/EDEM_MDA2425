# Based on console application that calculates the results of an investment.
# The application should incorporate a feature:
#   A menu with the following options: 
#     [1] Calculate an investment
#     [X] Exit 
#       In this case the program should display a goodbye message and exit

from session_2 import calculate_investment
import time
from termcolor import colored

def console():
  firstTime = True
  while True:
    if firstTime:
      print('''
▄▄ INVESTMENT APP ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                               █
█  Calculates the amount of an investment.      █
█                                               █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

What would you like to do?

[1] Calculate an investment
[X] Exit
    ''')
      firstTime = False
    else:
      time.sleep(1)
      print('''What do you want to do now?

[1] Calculate an investment
[X] Exit
    ''')
    option = input().lower()
    if option == '1':
      calculate_investment()
    elif option == 'x':
      print('''            
BEST WISHES WITH YOUR INVESTMENT!
''')
      break
    else:
      print(colored("Oops! That's not a valid option. Try again...", 'red'))

console()