import random
import re
import time

class Game(object):
    def __init__(self):
        movie_blank, shuffled_movie, movie_answer_comparable, full_movie = Game.getPuzzle(self)
        self.movie_blank = movie_blank
        self.shuffled_movie = shuffled_movie
        self.movie_answer_comparable = movie_answer_comparable
        self.full_movie = full_movie

    def newRound(self):
        movie_blank, shuffled_movie, movie_answer_comparable, full_movie = Game.getPuzzle(self)
        self.movie_blank = movie_blank
        self.shuffled_movie = shuffled_movie
        self.movie_answer_comparable = movie_answer_comparable
        self.full_movie = full_movie
        
    def getMovieList(self):
        movie_list = []

        with open('Movies.txt') as fp:
            for line in fp:
                movie_list.append(line.rstrip())
        return movie_list

    def getRandomMovie(self, movie_list):
        num_of_movies = len(movie_list)
        random_movie = movie_list[random.randint(1, num_of_movies)]
        return random_movie

    def getPuzzle(self, hard=False):
        movie_list = Game.getMovieList(self)
        input_movie = Game.getRandomMovie(self, movie_list)
        movie_lowercase = input_movie.lower()
        movie_no_specials = re.sub('[^0-9a-zA-Z ]', '', movie_lowercase)
        movie = movie_no_specials
        movie_listed = movie.split()
        movie_no_spaces = re.sub('[ ]', '/', movie_no_specials)
        movie_blank = re.sub('[0-9a-zA-Z]', '- ', movie_no_spaces)

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


# if __name__ == "__main__":
#     new_game = Game()
#     print(new_game.movie_blank)
#     print(new_game.shuffled_movie)
#     print(new_game.movie_answer_comparable)
#     print(new_game.full_movie)