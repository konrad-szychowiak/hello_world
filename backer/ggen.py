from sys import argv
from random import randint


def _random_pair(size):
    return randint(0, size - 1), randint(0, size - 1)


def _min_rich(size, constr):
    return constr * (size * (size - 1) // 2)


def _randomize_matrix(arr):
    l = len(arr)
    for i in range(_min_rich(l)):
        x, y = randint(0, l - 1), randint(0, l - 1)
        arr[x][y] = 0
        arr[y][x] = 0

    return arr


def list_to_matrix(s_list):
    n = len(s_list)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for el in s_list[i]:
            matrix[i][el] = matrix[el][i] = 1
    return matrix


class FriendList:
    def __init__(self, lista):
        self.lista = lista

    def friends_of(self, vertex):
        pos = self.lista.index(vertex)
        return [
            vertex,
            self.lista[pos - 1],
            self.lista[pos + 1]
        ]


def _rich(graph):
    tab = []
    for i in range(len(graph)):
        tab += graph[i]
    # print(tab)
    return len(tab)


def gen_list(size, constr):
    lista = [i + 1 for i in range(size - 1)]
    for i in range(size):
        a, b = _random_pair(size - 1)
        lista[a], lista[b] = lista[b], lista[a]
    lista = [*lista, 0]
    way = {}
    way[0] = [lista[0]]
    # print(lista)

    for i in range(size - 1):
        way[lista[i]] = [lista[i + 1]]

    #
    lista = FriendList(lista)

    while _rich(way) < _min_rich(size, constr):
        i = randint(1, size - 2)
        a, b = i, i
        forbiden = lista.friends_of(i)
        while a in forbiden or a in way[i] or b in way[i] or b in forbiden:
            a, b = _random_pair(size)
        way[i].append(a)
        way[i].append(b)

    for i in range(size):
        way[i] = sorted(list(set(way[i])))
        # a, b = _random_pair(len(way[i]))
        # way[i][a], way[i][b] = way[i][b], way[i][a]

    return(way)


class Generator:
    def __init__(self, size, density, hamiltonian=True):
        self.size = size
        self.list = gen_list(size, density)
        if not hamiltonian:
            self.list[size - 1] = []
        used = _rich(self.list)
        poss = _min_rich(size, 1)
        print(
            f"used {used} edges of {poss} edges possible ({(used/poss) *10000 // 10 / 10}%)"
        )

    def matrix(self):
        pass

    def print_list(self):
        for i in range(self.size):
            print(f"{i:3} :", " ".join(
                [f"→ {v}" for v in self.list[i]]))

        return self


if __name__ == '__main__':
    # _cli()
    print(
        gen_list(20, 0.5)
    )
