import webbrowser

# Bit improved version for finding an address just by typing in
# the result after 1 question
# ^_*


client_list = {
    'client0_address_Nexon': 'Minato City, Tokyo, Japan ',
    'client1_address_ChicagoIt': 'Chicago, IL ',
    'client2_address_US_Gov': 'Washington D. C., DC',
}
space = '\n'


# Client Info - Update as needed
# 0 = client0_address_Nexon
# 1 = client1_address_ChicagoIt
# 2 = client2_address_US_Gov

def ask_user():
    # user_address = input('Enter your address: ')
    print('Hello user...' + '\n')
    print('We currently have a total of ' + str(len(client_list)) + ' clients.' + '\n' +
          'Which address would you like to see?' + '\n')

    print('Client 0 : Nexon' + '\n' +
          'Client 1 : Chicago It Dept.' + '\n' +
          'Client 2: United States Gov' + '\n'
          )


def get_user_input():
    user_input_is_correct = True
    while user_input_is_correct:
        try:
            user_address = int(input('Please input the client\'s number #:  '))

            if user_address == 0:
                webbrowser.open('https://google.com/maps/place/' + client_list['client0_address_Nexon'])
            elif user_address == 1:
                webbrowser.open('https://google.com/maps/place/' + client_list['client1_address_ChicagoIt'])
            elif user_address == 2:
                webbrowser.open('https://google.com/maps/place/' + client_list['client2_address_US_Gov'])
            else:
                print('You\'ve exceed the maximum possible client list of, ' + str(len(client_list)) +
                      ' clients. Please try again! ')
                print(space)
                print('Client 0 : Nexon' + '\n' +
                      'Client 1 : Chicago It Dept.' + '\n' +
                      'Client 2: United States Gov' + '\n'
                      )
        except ValueError:
            print('You\'ve inputted a non-number, please try again')


def main():
    ask_user()
    get_user_input()


main()
