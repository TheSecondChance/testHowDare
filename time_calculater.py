from time import time

class TimeCalculator:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start the timer."""
        self.start_time = time()
    
    def stop(self):
        """Stop the timer."""
        self.end_time = time()
