from web_scrap_source import *
from colors import *

# Ask's the user for some basic information on what job/career they are looking for & the location
print('Once you have placed a Url, press Space then hit Enter to continue.')
user_job_want = input('Type the job/career you are looking for: ')
user_job_location = input('Type the city name you would like this job/career to be: ' + red + '\n'
                          'If your looking for a remote position type remote: ' + end)

user_site_combination = 'https://www.monster.com/jobs/search/?q=' + user_job_want + '&where=' + user_job_location

url = user_site_combination
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
#print(results.prettify())

job_elements = results.find_all('section', class_='card-content')
# .find_all() returns a iterable containing all the HTML for all the job listings displayed on the user's
#  page link that they have provided @ url

for job_elements in job_elements:
    '''  print(job_elements, end='\n'*2)

# This shows the info regarding the jobs in a bit more in-depth info
'''
    job_title_element = job_elements.find('h2', class_='title')
    company_element = job_elements.find('div', class_='company')
    location_element = job_elements.find('div', class_='location')

# RED = Job Title, # Green = Company Name, Blue = Job/Buisness Location
    print(red + str(job_title_element) + end)
    print(green + str(company_element) + end)
    print(blue + str(location_element) + end)



