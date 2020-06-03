from sys import stderr
from time import time

from .ggen import Generator
from .hamilton import hamilton
from .euler import euler

teda = [(i + 1) * 2 + 8 for i in range(10)][7:8]

print("Euler70", file=stderr)
for t in teda:
    print(t, end="; ", file=stderr)

    for i in range(5):
        graph = Generator(t, 0.7).lista()
        start = time()
        hamilton(graph)
        stop = time()
        timer = (stop - start)
        print(timer, end="; ", file=stderr)

    print(file=stderr)
