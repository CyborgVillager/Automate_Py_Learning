import requests

text_file_name = 'R&J.txt'
try:
    aquire_info = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    aquire_info.raise_for_status()
    open_file = open('R&J.txt', 'wb')
    for chunk in aquire_info.iter_content(10000):
        open_file.write(chunk)


    open_file.close()
    print('Success in aquiring info. To see the information please check ' + text_file_name)
except OSError:
    print('Failed to open the url, please check your connection to the url.')


