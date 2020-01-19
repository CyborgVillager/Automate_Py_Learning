import requests

#aquire_info = requests.get('https://kivy.org/doc/stable/api-kivy.html')
aquire_info = requests.get('https://kivy.org/dfdsfdsfds')
#print(aquire_info.raise_for_status())

try:
    aquire_info.aquire_info.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

