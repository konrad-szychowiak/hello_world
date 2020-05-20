from sys import stderr
from time import time

from .ggen import Generator
from .hamilton import hamilton

teda = [(i + 1) * 2 + 8 for i in range(10)]

print("Hamilton30", file=stderr)
for i in teda:
    print(i, end="; ", file=stderr)
    graph = Generator(i, 0.3).list

    for i in range(3):
        start = time()
        hamilton(graph)
        stop = time()
        timer = (stop - start)
        print(timer, end="; ", file=stderr)

    print(file=stderr)

print("Hamilton70", file=stderr)
for i in teda:
    print(i, end="; ", file=stderr)
    graph = Generator(i, 0.7).list

    for i in range(3):
        start = time()
        hamilton(graph)
        stop = time()
        timer = (stop - start)
        print(timer, end="; ", file=stderr)

    print(file=stderr)

print("Hamilton50", file=stderr)
for i in [20, 25, 30]:
    print(i, end="; ", file=stderr)
    graph = Generator(i, 0.5, False).list

    for i in range(3):
        start = time()
        hamilton(graph)
        stop = time()
        timer = (stop - start)
        print(timer, end="; ", file=stderr)

    print(file=stderr)
