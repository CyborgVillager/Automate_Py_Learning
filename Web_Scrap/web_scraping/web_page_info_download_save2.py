import requests , pyperclip

# User file name creation
user_file_name = input('Please enter a name for your file: ')
file_extension_txt = '.txt'
text_file =  user_file_name + file_extension_txt

# User Url Input
aquire_url = input( 'Please enter the url you wish to aquire text information from: ')
aquire_url = pyperclip.paste()


# How much info does the user wants
text_info_length = True
while text_info_length:
    try:
        text_info_length = int(input('Type the number of characters you would like to aquire: '))
        break
    except ValueError:
        print('Information must be an integer to proceed')

# Aquire requests from the user's input / write the info onto a file
# Check if there's any error for the url such as conneciton or mistype
# If so notify the user, if success update the user on its completion
try:
    aquire_info = requests.get(aquire_url)
    aquire_info.raise_for_status()

    open_file = open(text_file, 'wb')
    for chunk in aquire_info.iter_content(text_info_length):
        open_file.write(chunk)
    open_file.close()

    print('Success in aquiring info. To see the information please check ' + text_file)
except OSError:
    print('Failed to open the url, please check your connection to the url.')
except TypeError:
    print('Not correct information check your operation')

