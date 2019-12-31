# this program will launch a map using a browser/address

import webbrowser, sys
if len(sys.argv) > 1:

    # Getting the address from the cmd (aka Terminal)
    # Once the user has typed their address on the terminal  using this format -> python map_It.py ADDRESS

    address = ' '.join(sys.argv[1:])
    print(address)
# TODO: Get Address from clipboard
