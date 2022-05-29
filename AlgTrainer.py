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
    algorithms that the user got correctly once or have never seen before
Box 3:
    algorithms are moved here from box 2 once they are answered 3 times in a row
Box 4:
    algorithms waiting for review
Box 5:
    algorithms that the user got correctly during review
"""
import json # loading algorithms
import random
import Box
import Algorithm

REVIEW_COUNT = 8
# what percent of the time to pick from box 2 if there are algorithms in both box 2 and 3
BOX_2_PERCENTAGE = 70


class AlgTrainer:
    def __init__(self, file_path):
        self.boxes = self._createBoxes(file_path)
        self._initialAlgs()
        # self.lastAlg = "" TODO add in this

    def playRound(self):
        """
        playRound
        Tests the user on one algorithm
        Returns True if the user has learned every algorithm
        """
        box, alg = self.pickAlg()
        if box == -1:
            return True
        if box == 4:
            self._reviewSession()
            return False
        print(alg.getScramble())
        incorrect = input(
            "Enter any character if you got the algorithm wrong: ")
        if incorrect == "X":
            return True

        if incorrect:
            self.boxes[box].erase(alg)
            alg.reset()
            self.boxes[box].add(alg)
        else:
            alg.incrementStreak()
            if box == 1 or box == 2:
                alg.reset(wrongAns = False)
                self._move(alg, box, box+1)
            elif box == 3 and alg.getStreak() == 3:
                self.move(alg, 3, 4)
                self._addNewAlg()

        self.boxes[1].passRound()

    def pickAlg(self):
        """
        pickAlg
        Picks an algorithm to test the user on
        Returns the box and algorithm
        (box, algorithm)
        """
        if self._noAlgsLeft():
            return -1
        elif self.boxes[4].length() == REVIEW_COUNT:
            return 4
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

    def _noAlgsLeft(self):
        """
        _noAlgsLeft
        Determines if there are no algorithms in boxes 0-4, implying that the user has completed the 
        learning session.
        """
        for i in range(5):
            if self.boxes[i].length() != 0:
                return False
        return True

    def _algsInCycle(self):
        """
        _algsInCycle
        Finds the number of algorithms currently in boxes 1-3 (algorithm that are currently being learned)
        """
        return self.boxes[1].length() + self.boxes[2].length() + self.boxes[3].length()

    def _move(self, alg, startBox, endBox):
        """
        _move
        Receives an algorithm, the index of the box to remove it from,
        and the index of box to add it to
        """
        alg.reset(wrongAns=False)
        self.boxes[startBox].erase(alg)
        self.boxes[endBox].add(alg)
    
    def _addNewAlg(self):
        """
        _addNewAlg
        Adds a new algorithm into the rotation
        Picks from queuedAlgorithms if there are any in that box
        Else, picks one from box 0
        """
        if self.boxes[0]:
            self._move(random.choice(self.boxes[0]), 0, 2)

    def _removeAlg(self):
        """
        _removeAlg
        Takes an algorithm out of cycle
        Prefers to take an algorithm from box 2, then 1, then 3
        """
        if self.boxes[2]:
            self._move(self.boxes[2].getAlgorithm(), 2, 0)
        elif self.boxes[1]:
            self._move(self.boxes[1].getAlgorithm(), 1, 0)
        elif self.boxes[3]:
            self._move(self.boxes[3].getAlgorithm(), 3, 0)

    def _reviewSession(self):
        """
        _reviewSession
        Goes through the algorithms in box 4. Moves to box 1 if answered incorrectly,
        box 5 if answered correctly.
        """
        print("Review: ")
        random.shuffle(self.boxes[4])
        incorrectAlgs = []
        for alg in self.boxes[4]:
            print(alg.getScramble())
            incorrect = input(
            "Enter any character if you got the algorithm wrong: ")
            if incorrect:
                incorrectAlgs.append(alg)
            else:
                self._move(alg, 4, 5)

        for alg in incorrectAlgs:
            self.boxes[1].add(alg)

    def _createBoxes(self, file_path):
        """
        _createBoxes(self)
        Loads the algorithms from file_path
        Creates the boxes and fills box 2 with up to 8 algorithms
        """
        boxes = [Box.Box for i in range(6)]
        algs = {}
        with open(file_path) as f:
            algs = json.load(f)
        for alg in algs:
            boxes[0].add(Algorithm.Algorithm(alg, algs[alg]))
        return boxes

    def _initialAlgs(self):
        """
        _initialAlgs
        Picks the initial algorithms.
        Chooses up to 8 algorithms to move from box 0 to box 2
        """
        for i in range(min(self.boxes[0].length(), 8)): # TODO - remove magic number
            self._move(self.boxes[0].getAlgorithm(), 0, 2)