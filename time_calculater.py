from time import time

class TimeCalculator:
    def __init__(self):
        self.start = time()
    
    def elapsed(self):
        return time() - self.start