# Calculate and display prime numbers in given range.
import time

from functions import ask_input, is_prime, make_header

def display_primes_in_range():
  make_header('PRIME NUMBERS IN RANGE', 'Calculates and displays prime numbers in given range.', bg_color='magenta')

  # Iterate from the start until the end  
  start = ask_input('Enter the start of the range:')
  end = ask_input('Enter the end of the range:')
  
  print(f'''
Prime numbers between {start} and {end} are:''')
  counter = 0

  for num in range(start, end):
    if is_prime(num):
      time.sleep(0.1)
      if counter % 20 == 0 and counter != 0:
        print('')
      print(str(num) + ' ', end='', flush=True)
      counter += 1
  time.sleep(0.5)
  print(f"""
                    
A total of {counter} prime numbers were found.""")
  time.sleep(0.5)
  print('''
-----------------------
''')

# Call function to display prime numbers from 1 to 100
if __name__ == '__main__':
  display_primes_in_range()