from sys import argv
from time import sleep
from itertools import count, cycle

for i in cycle(argv[1:]):
    print(i)
    sleep(0.5)
