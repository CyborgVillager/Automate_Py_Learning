import requests

user_file_name = input('Please enter a name for your file: ')
file_extension_txt = '.txt'
text_file = user_file_name + file_extension_txt

try:
    aquire_info = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    aquire_info.raise_for_status()
    open_file = open(text_file, 'wb')
    for chunk in aquire_info.iter_content(10000):
        open_file.write(chunk)
    open_file.close()
    print('Success in aquiring info. To see the information please check ' + text_file)
except OSError:
    print('Failed to open the url, please check your connection to the url.')


