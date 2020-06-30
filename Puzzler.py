import random
import re
import time

def getMovieList():
    movie_list = []

    with open('Movies.txt') as fp:
        for line in fp:
            movie_list.append(line.rstrip())
    return movie_list

def getRandomMovie(movie_list):
    num_of_movies = len(movie_list)
    random_movie = movie_list[random.randint(1, num_of_movies)]
    return random_movie

def getPuzzle(hard=False):
    movie_list = getMovieList()
    input_movie = getRandomMovie(movie_list)
    movie_lowercase = input_movie.lower()
    movie_no_specials = re.sub('[^0-9a-zA-Z ]', '', movie_lowercase)
    movie = movie_no_specials
    movie_listed = movie.split()
    movie_no_spaces = re.sub('[ ]', '/', movie_no_specials)
    movie_blank = re.sub('[0-9a-zA-Z]', '_ ', movie_no_spaces)

    shuffled_movie_with_spaces = ''.join(random.sample(movie,len(movie)))
    shuffled_movie = re.sub('[ ]', '', shuffled_movie_with_spaces)

    new_scramble = ''
    for word in movie_listed:
        shuffled_word = ''.join(random.sample(word, len(word)))
        new_scramble = new_scramble + shuffled_word + ' '

    if hard:
        return movie_blank, shuffled_movie, movie, input_movie
    else:
        return movie_blank, new_scramble, movie, input_movie


if __name__ == "__main__":
    movie_blank, shuffled_movie, movie_answer_comparable, full_movie = getPuzzle()
    print(movie_blank)
    print(shuffled_movie)
    time.sleep(30)
    print(full_movie)
