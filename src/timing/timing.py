import atexit
import datetime
import functools
import time
from time import clock
import atexit

class Time():
    """
    1. current_time
    2. record execution time


    Use Example:
        start counting execution time...
        >>> Time.start()
        >>> atexit.register(Time.endlog)

        .. executing ..

        show elapsed time
        >>> Time.log("Start Program")
        ========================================
        0:00:00.000 - Start Program
        ========================================

        .. executing ..

        show elapsed time
        >>> Time.log("2 Program")
        ========================================
        0:00:02.000 - 2 Program
        ========================================

    """
    def __init__(self):
        pass

    @classmethod
    def current_time(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now

    @classmethod
    def secondsToStr(self, t):
        return "%d:%02d:%02d.%03d" % \
               functools.reduce(lambda ll, b: divmod(ll[0], b) + ll[1:],
                                [(t * 1000,), 1000, 60, 60])
    @classmethod
    def log(self, message_str, elapsed=None):
        line = "=" * 40

        operation_time = (
            f'{line}\n'
            f'{self.secondsToStr(clock())} - {message_str}\n'
            f'{line}\n'
            f'\n'
        )

        # if elapsed:
        #     print("Elapsed time:", elapsed)

        print(operation_time)

    @classmethod
    def start(self):
        self.start = clock()
        atexit.register(self.endlog)
        self.log("Start Program")

    @classmethod
    def endlog(self):
        """
        elapsed: count elapsed time

        """
        self.end = clock()
        elapsed = self.end - self.start
        self.log("End Program", self.secondsToStr(elapsed))

    @classmethod
    def now(self):
        return self.secondsToStr(clock())
