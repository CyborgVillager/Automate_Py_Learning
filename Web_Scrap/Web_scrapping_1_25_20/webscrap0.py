from web_scrap25_source import *

req = requests.get('https://docs.python.org/3/py-modindex.html')
print(type(req))
print(req.status_code == requests.codes['ok'])


