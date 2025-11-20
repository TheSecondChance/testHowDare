from time import time

class TimeChecker:
    def __init__(self):
        self.start_time = None
    
    def start(self):
        """Start the timer."""
        self.start_time = time()

    def stop(self):
        """Stop the timer and return the elapsed time."""
        if self.start_time is None:
            raise ValueError("Timer is not running.")
        elapsed_time = time() - self.start_time
        self.start_time = None
        return elapsed_time