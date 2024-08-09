"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
"""Machine for finding random words from a dictionary file.

    >>> wf = WordFinder("/path/to/test_words.txt")
    3 words read

    >>> wf.words
    ['cat', 'dog', 'porcupine']

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True
    """

def __init__(self, filepath):
        """Reads words from the file and reports the number of words read."""
        self.words = self.read_words(filepath)
        print(f"{len(self.words)} words read")

def read_words(self, filepath):
        """Reads words from a file and returns a list of words."""
        with open(filepath, 'r') as file:
            return [line.strip() for line in file]

def random(self):
        """Returns a random word from the list of words."""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments.

    >>> swf = SpecialWordFinder("/path/to/test_special_words.txt")
    4 words read

    >>> swf.words
    ['kale', 'parsnips', 'apple', 'mango']

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    """

    def read_words(self, filepath):
        """Reads words from a file, excluding blank lines and comments."""
        with open(filepath, 'r') as file:
            return [line.strip() for line in file
                    if line.strip() and not line.startswith("#")]
        
import doctest
doctest.testmod()