import signal
import time
import random
import time
import os, sys
import importlib

submissions = os.listdir()

def handler(signum, frame):
    print("Forever is over!")
    raise TimeoutError("Forever is over")

def get_submissions(directory="./Spring 2023/Code_one"):
    submissions = [file.replace(".py", "") for file in os.listdir(directory) if ".py" in file and file not in ["grading.py" or "solution.py"]]
    return submissions


        

random.seed(123456789)
signal.signal(signal.SIGALRM, handler)

submissions = get_submissions(sys.argv[1])


