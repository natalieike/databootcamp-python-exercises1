"""Word Finder: finds random words from a dictionary."""
import random
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Machine to return random words from a file. strips blank lines and comments that start with #
    
    >>> wf = SpecialWordFinder("./wordsComplex.txt")
    4 words read

    >>> wordList = [ 'kale', 'parsnips', 'apple', 'mango', ]
    >>> notWordList = [ '', '# Veggies', '# Fruits', '# Empty below', ]

    >>> wf.random() in wordList
    True
    
    >>> wf.random() in wordList
    True

    >>> wf.random() in wordList
    True

    >>> wf.random() == 'hello'
    False

    >>> wf.random() in notWordList
    False

    >>> wf.random() in notWordList
    False
    
    >>> wf.random() in notWordList
    False
    """

    def _readFile(self):
        with open(self.filename, encoding="utf-8") as f:
            self.wordList = []

            for line in f:
                stripLine = line.strip()
                if stripLine and stripLine[0] != '#':
                    self.wordList.append(stripLine)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
