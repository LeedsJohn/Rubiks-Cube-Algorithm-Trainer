"""
John Leeds
5/27/2022
WrongBox.py

Contains class WrongBox.
Algorithms are put in here when they are answered incorrectly.
"""
import random
import Algorithm

class wrongBox():
    def __init__(self):
        self.algorithms = {} # {algorithm: number of turns to show it in}

    def add(self, algorithm):
        """
        addAlgorithm
        Receives an algorithm to add to algorithms
        Chooses a random number between 1 and 3 and shows it after that number of turns
        """
        self.algorithms[algorithm] = random.randrange(1, 4)

    def erase(self, algorithm):
        """
        erase
        Receives an algorithm to remove from the dictionary
        """
        del self.algorithms[algorithm]

    def getMin(self):
        """
        getMin
        Returns the algorithm with the smallest number of turns
        or None if there is not an algorithm with a turn count <= 0
        """
        minTurns = 1
        minAlgorithm = None
        for algorithm in self.algorithms:
            if self.algorithms[algorithm] < minTurns:
                minTurns = self.algorithms[algorithm]
                minAlgorithm = algorithm
        return minAlgorithm

    def getRandomAlg(self):
        """
        getRandomAlg
        Returns a random algorithm
        """
        return self.algorithms[random.choice(list(self.algorithms.keys()))]
        
    def length(self):
        """
        length
        Returns the number of algorithms in the box
        """
        return len(self.algorithms)