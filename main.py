from time import time
from system import stderr
from rygg.classes import *
from rygg.dynamic import *
from rygg.heuristic import *
from rygg.brute_force import *

# 100_30
itemsLib = []
i = 0
with open('data/1.in') as f:
    c = 1
    for line in f:
        if c > 2:
            itemsLib.append(Item(*line.split(' '), _id=i))
            i += 1
        elif c == 1:
            c += 1
            capacity = int(line.strip())
        else:
            c += 1
            itemsNum = int(line.strip())


# 200_30
itemsLib5 = []
i = 0
with open('data/input5.txt') as f:
    c = 1
    for line in f:
        if c > 2:
            itemsLib5.append(Item(*line.split(' '), _id=i))
            i += 1
        elif c == 1:
            c += 1
            capacity5 = int(line.strip())
        else:
            c += 1
            itemsNum5 = int(line.strip())


# 300_30
itemsLib6 = []
i = 0
with open('data/input6.txt') as f:
    c = 1
    for line in f:
        if c > 2:
            itemsLib6.append(Item(*line.split(' '), _id=i))
            i += 1
        elif c == 1:
            c += 1
            capacity6 = int(line.strip())
        else:
            c += 1
            itemsNum6 = int(line.strip())

#
# capacity = int(input())
# itemsNum = int(input())
#
# itemsLib = []
#
#
# for i in range(itemsNum):
#     itemsLib.append(
#         Item(*input().split(' '), _id=i)
#     )


if __name__ == '__main__':
    # heuristic(capacity, itemsLib)
    # dynamic(capacity, itemsNum, itemsLib)
    start = time()
    brute_force(capacity, itemsNum, itemsLib)
    end = time()
    print("\nDla 100_30: ", end - start, file=stderr)

    start = time()
    brute_force(capacity5, itemsNum5, itemsLib5)
    end = time()
    print("\nDla 200_30: ", end - start, file=stderr)

    start = time()
    brute_force(capacity6, itemsNum6, itemsLib6)
    end = time()
    print("\nDla 300_30: ", end - start, file=stderr)
