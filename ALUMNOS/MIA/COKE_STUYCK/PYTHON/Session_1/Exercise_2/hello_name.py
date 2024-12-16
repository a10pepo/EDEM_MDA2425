# Show "Hello, [Name]" where the name is the value (str) of a variable
from functions import ask_input

def hello_name_function():
    name: str = ""
    name = ask_input('''
-----------------------

Enter your name:
''', str)
    
    print(f'''
-----------------------

Hello, {name}!

-----------------------
''')

if __name__ == '__main__':
    hello_name_function()