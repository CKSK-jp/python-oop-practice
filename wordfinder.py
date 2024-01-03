"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Instantiates a file that holds all the words in said dicts.
    
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random()
    'something'
    """
    
    def __init__(self, path_name):
        """instantiates the file path and list of words properties"""
        self.word_file = path_name
        self.word_list = self.count_words()
        
        
    def count_words(self):
        """Open file and create a list of words from file"""
        word_file = open(f'{self.word_file}')
        word_list = [word.strip() for word in word_file]
        print(f"{len(word_list)} words read")
        word_file.close()
        return word_list

    def random(self):
        """Return random word"""
        return choice(self.word_list)

    