# this program will launch a map using a browser/address

import webbrowser, sys,pyperclip
if len(sys.argv) > 1:

    # Getting the address from the cmd (aka Terminal)
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    # Get address from clipboard
    address = pyperclip.paste()
    # Once the user has typed their address on the terminal  using this format -> python map_It_1.py ADDRESS
    # They will be redirected to a google map service
webbrowser.open('https://google.com/maps/place/' + address)
