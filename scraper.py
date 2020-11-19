from bs4 import BeautifulSoup
from time import sleep, time
from random import randint
from IPython.core.display import clear_output
from warnings import warn
import requests

def scrapeMovies():

    years = [str(i) for i in range(1980, 2019)]
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    start_time = time()
    request_int = 0
    movie_list = []

    for year in years:  
        response = requests.get('http://www.imdb.com/search/title?release_date='
                                + year
                                + '&sort=num_votes,desc&page=1', headers=headers)
        elapsed_time = time() - start_time
        sleep(randint(2,5))
        request_int += 1

        print('Request: {}; Year: {}; Frequency: {} requests/s'.format(request_int, year,
                                                            request_int/elapsed_time))
        clear_output(wait=True)

        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(
                request_int, response.status_code))
        if request_int > 72:
            warn('Number of requests was greater than expected.')
            break

        page_html = BeautifulSoup(response.text, 'html.parser')
        movie_containers = page_html.find_all('div', class_='lister-item mode-advanced')

        for movie in movie_containers:
            movie_name = movie.h3.a.text
            movie_list.append(movie_name)
            
    return movie_list

def writeMovies(movie_list):
    for name in movie_list:
        with open('movies.txt', 'a') as output:
            output.write(name)
            output.write('\n')

if __name__ == "__main__":
    movie_list = scrapeMovies()
    writeMovies(movie_list)