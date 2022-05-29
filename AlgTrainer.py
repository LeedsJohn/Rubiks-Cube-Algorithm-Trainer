"""
John Leeds
5/27/2022
AlgTrainer.py

Contains five boxes of algorithms and helps the user learn them 
using an algorithm based off of the Leitner system
https://en.wikipedia.org/wiki/Leitner_system

Box 0:
    algorithms that the user has not seen yet
Box 1:
    algorithms that the user got wrong the last time they saw them
Box 2:
    algorithms that the user got correctly once
Box 3:
    algorithms are moved here from box 2 once they are answered 3 times in a row
Box 4:
    algorithms waiting for review
Box 5:
    algorithms that the user got correctly during review
"""
import random
import Box

REVIEW_COUNT = 8
BOX_2_PERCENTAGE = 70 # what percent of the time to pick from box 2 if there are algorithms in both box 2 and 3

class AlgTrainer:
    def __init__(self):
        self.boxes = self.createBoxes()
        self.queuedAlgorithms = []
        # self.lastAlg = "" TODO add in this

    def playRound(self):
        """
        playRound
        Tests the user on one algorithm
        """
        box, alg = self.pickAlg()
        incorrect = input("Enter any character if you got the algorithm wrong: ")
        if incorrect:
            self.boxes[box].erase(alg)
            alg[1].reset()
            self.boxes[box].add(alg)
        else:
            alg.increment()
            if box == 1:
                

    def pickAlg(self):
        """
        pickAlg
        Picks an algorithm to test the user on
        Returns the box and algorithm
        (box, algorithm)
        """
        if self._noAlgsLeft():
            return
        elif self.boxes[4].length() == REVIEW_COUNT:
            self._reviewSession()
            return
        elif self.boxes[1].urgentShowExists():
            return (1, self.algorithms[1].getMinAlgorithm())
        elif self.boxes[2].length() != 0 and self.boxes[3].length() == 0:
            return (2, self.algorithms[2].getAlgorithm())
        elif self.boxes[3].length() != 0 and self.boxes[2].length() == 0:
            return (3, self.algorithms[3].getAlgorithm())
        elif self.boxes[2].length() == 0 and self.boxes[3].length() == 0:
            return (1, self.algorithms[1].getMinAlgorithm())
        
        whichBox = random.randrange(0, 100)
        if whichBox < BOX_2_PERCENTAGE:
            return (2, self.boxes[2].getAlgorithm())
        return (3, self.boxes[3].getAlgorithm())