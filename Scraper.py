from bs4 import BeautifulSoup
from time import sleep, time
from random import randint
from IPython.core.display import clear_output
from warnings import warn
import requests


years_url = [str(i) for i in range(1980, 2018)]
headers = {"Accept-Language": "en-US, en;q=0.5"}
start_time = time()
requestint = 0
names = []

for year_url in years_url:  
    response = requests.get('http://www.imdb.com/search/title?release_date=' + year_url +
                            '&sort=num_votes,desc&page=1', headers=headers)
    sleep(randint(8,15))
    requestint += 1
    elapsed_time = time() - start_time
    print('Request: {}; Frequency: {} requests/s'.format(requestint,
                                                        requestint/elapsed_time))
    clear_output(wait=True)
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(
            requestint, response.status_code))
    if requestint > 72:
        warn('Number of requests was greater than expected.')
        break
    page_html = BeautifulSoup(response.text, 'html.parser')
    movie_containers = page_html.find_all('div', class_='lister-item mode-advanced')

    for movie in movie_containers:
        name = movie.h3.a.text
        names.append(name)

#print(movie_containers)

for name in names:
    with open('movies.txt', 'a') as output:
        output.write(name)
        output.write('\n')

