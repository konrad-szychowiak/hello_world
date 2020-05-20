from click import style

from .ggen import Generator


def hamilton(graph):
    start = 0
    counter = 0
    path = [start]
    visited = [False for i in range(len(graph))]
    # print(visited)
    visited[start] = True
    return cycle(graph, start, start, visited, path, counter)


def cycle(graph, current, start, visited, path, counter):
    # print(style(f" → {current}", fg="blue"), end="")
    visited[current] = True
    counter += 1
    for next in graph[current]:
        if next == start and counter == len(graph):
            return True
        if not visited[next]:
            if cycle(graph, next, start, visited, path, counter):
                path.append(current)
                return True
    visited[current] = False
    counter -= 1
    # print(style(" ←", fg="red"), end="")
    return False


if __name__ == '__main__':
    graph = Generator(20, 0.3).print_list().list
    hamilton(graph)
