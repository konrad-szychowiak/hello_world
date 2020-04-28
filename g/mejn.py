from copy import deepcopy
from ggen import Generator


def create_graph():
    """Tworzy graf"""
    v = int(input("Podaj ilosc wierzcholkow grafu:"))
    matrix = []
    for i in range(v):
        line = list(map(int, input(f"{i+1} linia:").split()))
        matrix.append(line)
    return matrix


def macierz_sasiedztwa(matrix):
    headings = [" "] + [f"V{j+1}" for j in range(len(matrix))]
    i = 1
    for line in matrix:
        line.insert(0, f"V{i}")
        i += 1


def lista_nastepnikow(matrix):
    result = []
    result2 = []
    n = len(matrix)
    for i in range(n):
        nastepniki = []
        for j in range(n):
            if matrix[i][j] == 1:
                nastepniki.append(j + 1)
        result.append([i + 1, " -> ".join(list(map(str, nastepniki)))])
        result2.append([i + 1, nastepniki])
    return result2


def tabela_krawedzi(matrix):
    n = len(matrix)
    table = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                table.append([i + 1, j + 1])
    return table


def dfs(v, result, successors):
    if v in result:
        return result
    result.append(v)
    for i in range(len(successors)):
        if successors[i][0] == v:
            nastepniki_v = successors[i][1]
            for el in nastepniki_v:
                result = dfs(el, result, successors)
            break
    return result


def przegladanie_dfs(successors):
    res = []
    for i in range(len(successors)):
        res = dfs(successors[i][0], res, successors)
    return res


def bfs(v, result, successors):
    for i in range(len(successors)):
        if successors[i][0] == v:
            nastepniki_v = successors[i][1]
            to_ignore = []
            for el in nastepniki_v:
                if el not in result:
                    result.append(el)
                else:
                    to_ignore.append(el)
            for el in nastepniki_v:
                if el not in to_ignore:
                    result = bfs(el, result, successors)
            break
    return result


def przegladanie_bfs(successors):
    res = []
    for i in range(len(successors)):
        nastepniki = successors[i][0]
        if nastepniki not in res:
            res.append(nastepniki)
            res = bfs(nastepniki, res, successors)
    return res


def dfs_sort_matrix(matrix):
    res = []
    # for i in range(len(matrix)):
    #     if matrix[i][i] == 0:
    #         matrix[i][i] = 1  # "szary"
    #     if


# FUNCS
def next_by_matrix(matrix, i):
    successors = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            successors.append(j + 1)
    return successors


def next_by_list(list, i):
    return list[i][1]


def next_by_table(table, i):
    successors = []
    for j in range(len(table)):
        if table[j][0] == i + 1:
            successors.append(table[j][1])
    return successors


# sortowanie BFS
# macierz


def create_in_degree_matrix(matrix):
    in_degree = []
    for i in range(len(matrix)):
        degree = matrix[i].count(-1)
        in_degree.append([i + 1, degree])
    return in_degree


def sort_bfs_by_matrix(matrix):
    in_degree = create_in_degree_matrix(matrix)
    return sortowanieBFS(in_degree, next_by_matrix, matrix)


# lista
def create_in_degree_list(list, n):
    in_degree = []
    flatten = sum([list[k][1] for k in range(len(list))], [])
    for i in range(n):
        degree = flatten.count(i + 1)
        in_degree.append([i + 1, degree])
    return in_degree


def next_by_list(list, i):
    return list[i][1]


def sort_bfs_by_list(list, n):
    in_degree = create_in_degree_list(list, n)
    return sortowanieBFS(in_degree, next_by_list, list)


# tabela
def create_in_degree_table(table, n):
    in_degree = []
    flatten = [table[k][1] for k in range(len(table))]
    for i in range(n):
        degree = flatten.count(i + 1)
        in_degree.append([i + 1, degree])
    return in_degree


def sort_bfs_by_table(table, n):
    in_degree = create_in_degree_table(table, n)
    return sortowanieBFS(in_degree, next_by_table, table)


def lower_degree(successors, in_degree):
    for i in range(len(in_degree)):
        if in_degree[i][0] in successors:
            in_degree[i][1] -= 1
    return in_degree


def sortowanieBFS(in_degree, find_next, data):
    result = []
    while max([in_degree[k][1] for k in range(len(in_degree))]) > -1:
        for i in range(len(in_degree)):
            if in_degree[i][1] == 0:
                in_degree[i][1] = -1
                result.append(i + 1)
                successors = find_next(data, i)
                in_degree = lower_degree(successors, in_degree)
    return " -> ".join(list(map(str, result)))
