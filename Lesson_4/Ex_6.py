from sys import argv
from time import sleep
from itertools import count

for i in count(int(argv[1])):
    print(i)
    sleep(0.5)
