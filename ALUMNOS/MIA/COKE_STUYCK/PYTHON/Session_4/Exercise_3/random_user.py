import requests

def random_user_request():
    answer = requests.get('https://randomuser.me/api')
    print('''
-----------------------
''')
    print('Generated random user:')
    print(answer.json()['results'][0]['name']['first'] + ' ' + answer.json()['results'][0]['name']['last'])
    print('''
-----------------------
''')

if __name__ == '__main__':
    random_user_request()