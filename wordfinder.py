"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine to return random words from a file.
    
    >>> wf = WordFinder("./wordsShortList.txt")
    15 words read

    >>> wordList = [ 'A', 'a', 'aa', 'aardvark', 'mingler', 'minglingly', 'mingy', 'minhag', 'taboret', 'tabouret', 'zymotoxic', 'zythem', 'Zyzomys', 'Z', 'z', ]

    >>> wf.random() in wordList
    True
    
    >>> wf.random() in wordList
    True

    >>> wf.random() in wordList
    True

    >>> wf.random() == 'hello'
    False
    """

    def __init__(self, fileName):
        self.filename = fileName
        self._readFile()
        print(f'{len(self.wordList)} words read')

    def _readFile(self):
        with open(self.filename, encoding="utf-8") as f:
            self.wordList = list(f)

    def random(self):
        randomNum = random.randint(0, len(self.wordList) -1 )
        return self.wordList[randomNum].strip()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
