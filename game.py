import random
import re
import time


class Game(object):
    movie_list: list
    full_movie_title: str
    sanitized_title: str
    movie_blank: str
    shuffled_title: str
    
    
    def __init__(self):
        self.getMovieList()
        self.newPuzzle()


    def getMovieList(self):
        movie_list = []
        with open("Movies.txt") as fp:
            for line in fp:
                movie_list.append(line.rstrip())
        self.movie_list = movie_list


    def getRandomMovie(self):
        num_of_movies = len(self.movie_list)
        random_movie = self.movie_list[random.randint(1, num_of_movies)]
        self.full_movie_title = random_movie

        
    def newPuzzle(self, hard=False):
        self.getRandomMovie()
        self.sanitizeMovieName(self.full_movie_title)
        self.generateBlanks(self.sanitized_title)
        self.scrambleTitle(self.sanitized_title)
    
    
    def sanitizeMovieName(self, movie_title):
        movie_lowercase = movie_title.lower()
        movie_no_specials = re.sub("[^0-9a-zA-Z ]", "", movie_lowercase)
        self.sanitized_title = movie_no_specials
    

    def generateBlanks(self, sanitized_title):
        movie_no_spaces = re.sub("[ ]", "/", self.sanitized_title)
        movie_blank = re.sub("[0-9a-zA-Z]", "- ", movie_no_spaces)
        self.movie_blank = movie_blank
        
        
    def scrambleTitle(self, sanitized_title):
        new_scramble = ""
        movie_listed = sanitized_title.split()
        for word in movie_listed:
            shuffled_word = "".join(random.sample(word, len(word)))
            new_scramble = new_scramble + shuffled_word + " "
        self.shuffled_title = new_scramble

if __name__ == "__main__":
    new_game = Game()
    print(new_game.full_movie_title)
    print(new_game.sanitized_title)
    print(new_game.movie_blank)
    print(new_game.shuffled_title)
