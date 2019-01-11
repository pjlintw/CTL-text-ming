

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"


class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name}. Surprise'

kevin_hart = Comedian('Hart', 'Kevin', 36)

def current_time():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now

import datetime
import time
operation_start = time.time()
time.sleep(0.5)
operation_end = time.time()

operation_time = operation_end - operation_start

operation_message = (
    f"[Finished in {operation_time}s]\n"
    f"{current_time()}"
)

import atexit
from time import clock

import functools
def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        functools.reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "="*40
def log(s, elapsed=None):
    line = "=" * 40

    operation_time = (
        f'{line}\n'
        f'{secondsToStr(clock())} - {s}\n'
        f'{line}\n'
        f'\n'
    )

    if elapsed:
        print("Elapsed time:", elapsed)

    print(operation_time)

def endlog():
    end = clock()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

def now():
    return secondsToStr(clock())


start = clock()
time.sleep(0.2)
atexit.register(endlog)
log("Start Program")
print()