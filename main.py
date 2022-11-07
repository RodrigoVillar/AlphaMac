import game
import multiprocessing as mp
import time
import threading
import sys

if __name__ == "__main__":
    # Create game instance
    # Run game
    game = game.Game()

    secs = game._secs
    
    game.start()

    time.sleep(secs)

    game.raise_exception()

    print("\nYour score was: " + str(game.get_score()))

    sys.exit("End of Game!")
