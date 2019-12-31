import webbrowser
# Bit improved version for finding an address just by typing in
# the result after 1 question
# ^_*

def ask_user():
    user_address = input('Enter your address: ')
    webbrowser.open('https://google.com/maps/place/' + user_address)


def main():
    ask_user()

main()