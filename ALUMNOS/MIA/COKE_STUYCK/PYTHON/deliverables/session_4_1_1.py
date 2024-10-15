# Calculate and display prime numbers in given range.
import time
from termcolor import colored

from functions import ask_input, is_prime

def display_primes_in_range():
  # Iterate from the start until the end
  print(f'''
▄▄ PRIME NUMBERS IN RANGE ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                               █
█  Calculates and displays                      █
█  prime numbers in given range.                █
█                                               █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')
  
  start = ask_input('Enter the start of the range:')
  end = ask_input('Enter the end of the range:')
  
  print(f'''
Prime numbers between {start} and {end} are:''')
  counter = 0

  for num in range(start, end):
    if is_prime(num):
      #time.sleep(0.02)
      if counter % 20 == 0 and counter != 0:
        print('')
      print(str(num) + ' ', end='', flush=True)
      counter += 1
  #time.sleep(0.5)
  print(f"""
                    
A total of {counter} prime numbers were found.
""")
  #time.sleep(0.5)
  print(f"""
THAT'S ALL!
""")

# Call function to display prime numbers from 1 to 100
display_primes_in_range()