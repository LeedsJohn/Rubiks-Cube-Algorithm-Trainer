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
    algorithms that the user got correctly during the review session
"""
import random
import Box
import WrongBox

REVIEW_COUNT = 8
BOX_2_PERCENTAGE = 70 # what percent of the time to pick from box 2 if there are algorithms in both box 2 and 3

class AlgTrainer:
    def __init__(self):
        self.boxes = self.createBoxes()
        self.queuedAlgorithms = []
        self.lastAlg = ""

    def pickAlg(self):
        """
        pickAlg
        Draws a card from the algorithms
        If box 3 contains REVIEW_COUNT algorithms, initiates a review session
        Else if there is a card that was answered incorrectly that has a turn count < 1, this is selected
        Else:
            If there are algorithms in both box 1 and 2, picks an algorithm from box 1 70% of the time
            If one of the boxes is empty, picks an algorithm from the other
        """
        minWrongBox = self.boxes[1].getMin()
        notMinBox = self._pickAlgorithmNotMin()
        if self.boxes[3].length() >= REVIEW_COUNT:
            self._review_session()
        elif minWrongBox:
            return minWrongBox
        elif notMinBox:
            return notMinBox
        else:
            print("Uhhh fix this")
            return

    def _pickAlgorithmNotMin(self):
        """
        _pickAlgorithmNotMin
        Selects an algorithm when there is not one to select from box 1
        """
        box_selection = random.randrange(0, 100)

        box2HasOption = self.boxes[2].length() != 0 and self.boxes[2].getFirstAlgorithmName() != self.lastAlg
        box3HasOption = self.boxes[3].length() != 0 and self.boxes[3].getFirstAlgorithmName() != self.lastAlg

        if box2HasOption and (not box3HasOption or box_selection <= BOX_2_PERCENTAGE):
            return self.boxes[2].getAlgorithm()
        elif box3HasOption and (not box2HasOption or box_selection > BOX_2_PERCENTAGE):
            return self.boxes[3].getAlgorithm()
        
        return None

    def _insertAlg(self, boxIndex, alg):
        """
        _insertAlg
        Adds a new algorithm into a box
        Receives the index of the box to insert into
        Receives the algorithm to insert
        """
        self.boxes[boxIndex].add(alg)

    def _removeAlg(self):
        """
        _removeAlg
        Selects an algorithm to move back into box 0
        Prefers to pick from the lowest box possible, can't pick from box 4
        """
        if self.boxes[1].length() != 0:
            return self.boxes[1].getRandomAlg()
        if self.boxes[2].length() != 0:
            return self.boxes[2].getAlgorithm()
        return self.boxes[3].getAlgorithm()

    def _review_session(self):
        pass

    def _algorithmsInRotation(self):
        """
        _algorithmsInRotation
        Returns the number of algorithms that are currently being learned.
        These are the algorithms in boxes 1, 2, and 3
        """
        return sum(self.boxes[1].length(), self.boxes[2].length(), self.boxes[3].length())