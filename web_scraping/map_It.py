# this program will launch a map using a browser/address

import webbrowser, sys
if len(sys.argv) > 1:

    # Getting the address from the cmd (aka Terminal)
    address = ' '.join(sys.argv[1:])
    print(address)
# TODO: Get Address from clipboard
