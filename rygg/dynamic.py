from rygg.classes import *


class Ryggsakk:
    def __init__(self, _matrix, _trace, _value):
        self.matrix = _matrix
        self.trace = _trace
        self.value = _value


def _set_content(i, j, table, w, p):
    upper = table[i - 1][j]
    prev = table[i - 1][j - w[i]] + p[i]

    if j < w[i]:
        table[i][j] = upper
    else:
        table[i][j] = upper if upper > prev else prev


def _trace_content(items, x, y, table, w, traceback):
    # print("%3i | %3i | %3s " % (x, y, table[x][y]), end="| ")

    if x == 0:
        return traceback

    if table[x][y] == table[x - 1][y]:
        # print("X")
        return _trace_content(items, x - 1, y, table, w, traceback)

    else:
        # print(items[x - 1].value)
        return _trace_content(items, x - 1, y - w[x], table, w, [x] + traceback)


def dynamic(size, itemsc, items):
    w = [0, *[item.size for item in items]]
    p = [0, *[item.value for item in items]]
    id = [0, *[item.id for item in items]]
    # table = [[0 for i in range(size)]] + [[0] for i in range(itemsc)]
    table = [[0 for j in range(size)] for i in range(itemsc + 1)]
    # print(len(table), len(table[len(table) - 1]))

    for _row in range(1, len(table)):
        for _cap in range(1, size):
            table[_row][_cap] = table[_row - 1][_cap] if _cap < w[_row] else \
                max(table[_row - 1][_cap], table[_row - 1]
                    [_cap - w[_row]] + p[_row])

    print(table[len(table) - 1][len(table[len(table) - 1]) - 1])

    trace = _trace_content(items,
                           len(table) - 1, len(table[len(table) - 1]) - 1, table, w, [])

    # print(trace, sum([p[x] for x in trace]))

    print(
        # trace,
        # sum([p[x] for x in trace]),
        [id[item] for item in trace]
    )

    # for row in table:
    #     print("".join([
    #         f"{val};" for val in row
    #     ]))
