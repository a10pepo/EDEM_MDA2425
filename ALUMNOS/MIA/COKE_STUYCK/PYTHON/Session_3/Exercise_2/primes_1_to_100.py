import time
from functions import is_prime, make_header

# Calculate and display prime numbers from 1 to 100.
def display_primes_1_to_100():
  make_header('PRIME NUMBERS FROM 1 TO 100', 'Calculates and displays prime numbers from 1 to 100.', bg_color='magenta')
  # Iterate from numbers 2 until 100 (1 is not a prime number)
  for num in range(2, 101):
    if is_prime(num):
      print(str(num) + ' ', end='', flush=True)
      time.sleep(0.1)
  time.sleep(0.5)
  print('''

Keep up with the serch for primes!

-----------------------
''')

# Call function to display prime numbers from 1 to 100
if __name__ == '__main__':
  display_primes_1_to_100()