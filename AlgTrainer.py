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

import Box
import WrongBox

REVIEW_COUNT = 8

class AlgTrainer:
    def __init__(self):
        self.boxes = self.createBoxes()
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
        if self.boxes[3].length() >= REVIEW_COUNT:
            self.review_session()
        elif minWrongBox:
            return minWrongBox
        elif self.box[1].length() != 

    def review_session(self):
        pass