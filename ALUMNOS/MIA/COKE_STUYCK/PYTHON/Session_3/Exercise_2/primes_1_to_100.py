from functions import is_prime

# Calculate and display prime numbers from 1 to 100.
def display_primes_until_100():
  # Iterate from numbers 2 until 100 (1 is not a prime number)
  print('''
▄▄ PRIME NUMBERS FROM 1 TO 100 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                               █
█  Calculates and displays                      █
█  prime numbers from 1 to 100.                 █
█                                               █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')
  for num in range(2, 101):
    if is_prime(num):
      print(str(num) + ' ', end='')
  print("""
                    
THAT'S ALL!
""")

# Call function to display prime numbers from 1 to 100
display_primes_until_100()