import requests

aquire_info = requests.get('https://kivy.org/doc/stable/api-kivy.html')
print(type(aquire_info))

aquire_info.status_code == requests.codes.ok

print(aquire_info.status_code )

print('There\'s over ' + str(len(aquire_info.text)) + ' lines of text/info')
print('\n')
print(str(aquire_info.text[:300]))