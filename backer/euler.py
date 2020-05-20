def find_neighbours(v: int, matrix: list):
    neighbours = [i for i in range(len(matrix[v])) if matrix[v][i] == 1]
    return neighbours


def dfs_euler(v: int, matrix: list, solution: list):
    neighbours = find_neighbours(v, matrix)
    for u in neighbours:
        if matrix[v][u] == 1:
            matrix[v][u] = 0
            matrix[u][v] = 0
            matrix = dfs_euler(u, matrix, solution)
    solution.append(v)
    return matrix


def euler(graph: list):  # graph -> matrix
    solution = []
    dfs_euler(graph[0][0], graph, solution)
    return " -> ".join(list(map(str, solution)))
