"""
John Leeds
5/27/2022
Box.py

Contains datastructure Box which holds Algorithms
"""
import random
import Algorithm

class Box:
    def __init__(self):
        self.algorithms = []
    
    def erase(self, alg):
        """
        erase()
        Receives an algorithm to remove from the algorithms (list)
        """
        if alg in self.algorithms:
            self.algorithms.remove(alg)
    
    def add(self, algorithm):
        """
        add()
        Receives an algorithm to add to the list of algorithms (Algorithm)
        """
        self.algorithms.append(algorithm)
    
    def pop(self):
        """
        pop()
        Calls pop on algorithms
        """
        return self.algorithms.pop()

    def length(self):
        """
        length
        Returns the number of algorithms in the box
        """
        return len(self.algorithms)

    def getAlgorithm(self):
        """
        getAlgorithm
        Returns a randomly selected algorithm
        """
        return random.choice(self.algorithms)
    
    def getMinAlgorithm(self):
        """
        getMinAlgorithm
        Returns the algorithm with the minimum turnsUntilShow
        """
        minTurns = self.algorithms[0].getTurnsUntilShow()
        minAlg = self.algorithms[0]

        for alg in self.algorithms:
            if alg.getTurnsUntilShow() < minTurns:
                minTurns = alg.getTurnsUntilShow()
                minAlg = alg
        return minAlg

    def urgentShowExists(self):
        """
        urgentShowExists
        Returns true if there is an algorithm in the box
        where turnsUntilShow <= 0
        """
        for alg in self.algorithms:
            if alg.getTurnsUntilShow() <= 0:
                return True
        return False

    def passRound(self):
        """
        passRound
        Subtracts 1 from every algorithms turnsUNtilShow
        """
        for alg in self.algorithms:
            alg.decrementTurnsUntilShow()

    def shuffle(self):
        """
        shuffle
        Shuffles the algorithms
        """
        random.shuffle(self.algorithms)