from time import time

class TimeChecker:
    def __init__(self):
        self.start_time = None
    
    def start(self):
        """Start the timer."""
        self.start_time = time()

    def check_elapsed(self):
        """Check the elapsed time since the timer was started."""
        if self.start_time is None:
            raise ValueError("Timer has not been started.")
        return time() - self.start_time