while True:
    print('Who are you? ')
    name = input('My name is: ')
    if name != 'Jonathan':
        continue
    print('Welcome ' + name + ' Please enter your password: ')
    password =  input('Password: ')
    if password == 'password':
        break
print('Access granted...')