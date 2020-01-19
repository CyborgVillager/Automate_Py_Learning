from web_scrap_source import *

print('Once you have placed a Url, press Space then hit Enter to continue.')
user_site_scrap = input('Enter Monster.com Url to continue: ')

url = user_site_scrap
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())


