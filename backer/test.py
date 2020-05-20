from sys import stderr
from time import time

from .ggen import Generator
from .hamilton import hamilton

teda = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Hamilton30", end="; ", file=stderr)
for i in teda:
    print(i, end="; ", file=stderr)
    graph = Generator(i, 0.3).list

    timer = 0
    for i in range(3):
        start = time()
        hamilton(graph)
        stop = time()
        timer += (stop - start)

    print(timer / 3, end="; ", file=stderr)

    print(file=stderr)

print("Hamilton70", end="; ", file=stderr)
for i in teda:
    print(i, end="; ", file=stderr)
    graph = Generator(i, 0.7).list

    timer = 0
    for i in range(3):
        start = time()
        hamilton(graph)
        stop = time()
        timer += (stop - start)

    print(timer / 3, end="; ", file=stderr)

    print(file=stderr)

print("Hamilton50", end="; ", file=stderr)
for i in [20, 25, 30]:
    print(i, end="; ", file=stderr)
    graph = Generator(i, 0.5, False).list

    timer = 0
    for i in range(3):
        start = time()
        hamilton(graph)
        stop = time()
        timer += (stop - start)

    print(timer / 3, end="; ", file=stderr)

    print(file=stderr)
