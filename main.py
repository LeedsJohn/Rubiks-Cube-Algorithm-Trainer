"""
John Leeds
5/29/2022
main.py

Main file for algorithm trainer.
"""

import AlgTrainer

def main():
    game = AlgTrainer.AlgTrainer("WV.json")
    while True:
        if game.playRound():
            break
    
if __name__ == "__main__":
    main()