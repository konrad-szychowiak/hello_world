import sys
n, m = input().split()
n, m = int(n), int(m)

diag = list(map(lambda x: 0, range(m)))
adia = list(map(lambda x: 0, range(m)))

for _n in range(n):
    line = input().split()
    for _m in range(m):
        diag[_m] += int(line[_m])
        adia[_m+_n] += int(line[_m])
    diag = [0] + diag
    adia = adia + [0]

diag.sort()
adia.sort()

print(   diag[-1] if diag[-1] > adia[-1] else adia[-1]   )
