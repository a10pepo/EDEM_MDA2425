import time
from functions import is_leap_year
    
year_list = [2020, 2021, 2022, 2023, 2024, 2025]

print('''
▄▄ LEAP YEAR OR NOT? ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                               █
█  Given a list of years,                       █
█  checks if each one is a leap year or not.    █
█                                               █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')

print('List of years; ')
print(year_list, '\n')

# Identify from a list of years if they are leap years.
for year in year_list:
  time.sleep(0.5)
  print(f'{year}: It is a leap year' if is_leap_year(year) else f'{year}: It is not a leap year')

print('')
