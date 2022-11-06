import game
import multiprocessing as mp
import time

if __name__ == "__main__":
    # Create game instance
    # Run game
    game = game.Game()

    secs = game._secs
    
    p = mp.Process(target=game.run)
    p.start()

    time.sleep(secs)

    p.terminate()

    p.join()

    print("Your score was: " + str(game.get_score()))

