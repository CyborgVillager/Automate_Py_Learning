# This prgram asks the user for their name


def ask_user():
    print('Hello user, ^_^ how may I call you? ')
    ask_user = input('Your Name: ')
    print('\n')
    print('Ah, thats a nice name ' + ask_user + ' has a nice ring tone to it!')
    print('A fun fact, your name length is ' + str(len(ask_user)) + ' ^_*')

    def ask_user_for_age():
        print('By the way ' + ask_user + ' how old are you? ')
        ask_user_age = float(input('My age is: '))
        print('Nice your age is: ' + str(round(ask_user_age)) + ' years old')
    ask_user_for_age()


def spacing():
    print('\n')








