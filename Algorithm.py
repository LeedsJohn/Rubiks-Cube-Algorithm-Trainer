"""
John Leeds
5/27/2022
Algorithm.py
Contains a class Algorithm
"""
import random # select random scramble

class Algorithm:
    def __init__(self, name, scrambles):
        """
        Constructor
        Receives the name of the algorithm (string)
        Receives scrambles that lead to that algorithm (list of strings)
        """
        self.name = name
        self.scrambles = scrambles
        self.streak = 0
        self.turnsUntilShow = None

    def increment(self):
        """
        increment()
        Increases streak by 1
        Decreases turnsUntilShow by 1 if applicable
        """
        self.streak += 1
        if self.turnsUntilShow:
            self.turnsUntilShow -= 1
    
    def reset(self):
        """
        Sets streak to 0
        """
        self.streak = 0

    # GETTERS
    def getName(self):
        return self.name
    def getStreak(self):
        return self.streak
    def getTurnsUntilShow(self):
        return self.turnsUntilShow
    def getScramble(self):
        """
        getScramble()
        Returns one randomly selected scramble.
        """
        return random.choice(self.scrambles)