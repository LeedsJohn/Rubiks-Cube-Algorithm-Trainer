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
    
    def pop(self, index):
        """
        pop()
        Receives an index to remove from the algorithms (list)
        Returns the algorithm
        """
        return self.algorithms.pop(index)
    
    def add(self, algorithm):
        """
        add()
        Receives an algorithm to add to the list of algorithms (Algorithm)
        """
        self.algorithms.append(algorithm)
    
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

    def getFirstAlgorithmName(self):
        """
        getFirstAlgorithmName
        Returns the name of the first algorithm from the algorithm list
        """
        if self.algorithms:
            return self.algorithms[0].getName()
        return ""