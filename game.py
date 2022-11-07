# Environment variables
from dotenv import load_dotenv
import os
from os.path import join, dirname
import random
import threading
import ctypes

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

addition = int(os.environ.get("addition"))
multiplication = int(os.environ.get("multiplication"))
subtraction = int(os.environ.get("subtraction"))
division = int(os.environ.get("division"))

operations = {
    "add": addition,
    "sub": subtraction,
    "mul": multiplication,
    "div": division
}

used_operations = [i for i in operations.keys() if operations[i] > 0]

add_x1 = int(os.environ.get("add_x1"))
add_x2 = int(os.environ.get("add_x2"))
add_x3 = int(os.environ.get("add_x3"))
add_x4 = int(os.environ.get("add_x4"))

mul_x1 = int(os.environ.get("mul_x1"))
mul_x2 = int(os.environ.get("mul_x2"))
mul_x3 = int(os.environ.get("mul_x3"))
mul_x4 = int(os.environ.get("mul_x4"))

decimals = int(os.environ.get("decimals"))
decimal_places = os.environ.get("decimal_places")

penalize_errors = os.environ.get("penalize_errors")

secs = int(os.environ.get("time"))

class Game(threading.Thread):

    def __init__(self):
        # Represents players current score
        threading.Thread.__init__(self)

        self._score = 0
        self._secs = secs

        self._run = True

    def prompt(self, x, y, op):
        try:
            print(str(x) + op + str(y) + ": ")
            user_val = int(input())
            return user_val
        except:
            pass

    def run(self):
        while self._run:
            # First choose between add, sub, mul, div
            rand_index = random.randrange(len(used_operations))
            op = used_operations[rand_index]

            if decimals == 0:
                if op == "add": # Addition
                    x = random.randrange(add_x1, add_x2)
                    y = random.randrange(add_x1, add_x2)
                    response = self.prompt(x, y, " + ")
                    if response != x + y:
                        if penalize_errors == 1:
                            self._score -= 1
                        print("Wrong Answer!")
                    else:
                        print("Correct Answer!")
                        self._score += 1
                elif op == "sub": # Subtraction
                    x = random.randrange(add_x1, add_x2)
                    y = random.randrange(add_x1, add_x2)
                    response = self.prompt(x, y, " - ")
                    if response != x - y:
                        if penalize_errors == 1:
                            self._score -= 1
                        print("Wrong Answer!")
                    else:
                        print("Correct Answer!")
                        self._score += 1
                elif op == "mul": # Multiplication
                    x = random.randrange(mul_x1, mul_x2)
                    y = random.randrange(mul_x3, mul_x4)
                    response = self.prompt(x, y, " * ")
                    if response != x * y:
                        if penalize_errors == 1:
                            self._score -= 1
                        print("Wrong Answer!")
                    else:
                        print("Correct Answer")
                        self._score += 1
                else: # Division
                    x = random.randrange(mul_x1, mul_x2)
                    y = random.randrange(mul_x3, mul_x4)
                    while y % x != 0:
                        x = random.randrange(mul_x1, mul_x2)
                        y = random.randrange(mul_x3, mul_x4)
                    response = self.prompt(y, x, "/")
                    if response != y / x:
                        if penalize_errors == 1:
                            self._score -= 1
                            print("Wrong Answer!")
                    else:
                        print("Correct Answer!")
                        self._score += 1
            else:
                if op == "add": # Addition
                    pass
                elif op == "sub": # Subtraction
                    pass
                elif op == "mul": # Multiplication
                    pass
                else: # Division
                    pass


    def get_score(self):
        return self._score

    def raise_exception(self):
        thread_id = self.get_id()
        self._run = False
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
            ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

    def get_id(self):
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
