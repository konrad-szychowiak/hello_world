from sys import argv
from copy import deepcopy

from tabulate import tabulate
from click import style

# from .ggen import Generator
from .euler import euler
from .hamilton import hamilton


# GRAPH REPRESENTATION


def read_graph():
    """Tworzy graf"""
    v = int(input("Podaj ilosc wierzcholkow grafu:"))
    print("Podaj kolejne wiersze macierzy sasiedztwa:")
    matrix = []
    for i in range(v):
        line = list(map(int, input(f"{i + 1} linia:").split()))
        matrix.append(line)
    return matrix


def macierz_sasiedztwa(matrix: list):
    print(style("\nMacierz sasiedztwa", fg='blue'))
    headings = [" "] + [f"V{j}" for j in range(len(matrix))]
    i = 0
    for line in matrix:
        line.insert(0, f"V{i}")
        i += 1
    print(tabulate(matrix, headers=headings, tablefmt='orgtbl'))


def lista_nastepnikow(matrix: list):
    print(style("\nLista nastepnikow", fg='blue'))
    result = []
    result2 = []
    n = len(matrix)
    for i in range(n):
        nastepniki = []
        for j in range(n):
            if matrix[i][j] == 1:
                nastepniki.append(j)
        result.append([i, " -> ".join(list(map(str, nastepniki)))])
        result2.append([i, nastepniki])
    print(tabulate(result, headers=['V', 'lista'], tablefmt='orgtbl'))
    return result2


def tabela_krawedzi(matrix):
    print(style("\nTabela krawedzi", fg='blue'))
    n = len(matrix)
    table = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                table.append([i, j])
    print(tabulate(table, headers=["out", "in"], tablefmt='orgtbl'))
    return table


def next_by_list(list, i):
    return list[i][1]


# MAIN --- HOME #

def main(argv):
    while True:
        try:
            x = int(input("\nWybierz opcje:\n0.Wyjscie\n"
                          "1.Wygenerowac graf losowo\n"
                          "2.Podac macierz sasiedztwa z klawiatury\n-> "))
        except ValueError:
            print(style("[!] Nalezy podac liczbe z zakresu 0..2", fg='red'))
            continue

        if x == 0:
            break
        elif x == 1:
            _gen_size = int(input("Podaj liczbę wierzchołków grafu -> "))
            try:
                density = int(input("\nWybierz nasycenie (1/2/3):\n1. 30%\n"
                                    "2.70%\n"
                                    "3. Graf nie-hamiltonowski, nasycenie 50%\n-> "))
            except ValueError:
                print(style("[!] Nalezy podac liczbe z zakresu 1..3", fg='red'))
                continue

            hamiltonian = False if density == 3 else True
            graph = Generator(_gen_size, density, hamiltonian)
            matrix = graph.matrix()
            lista = graph.lista()

        elif x == 2:
            matrix = read_graph()
        else:
            print(style("[!] Nalezy podac liczbe z zakresu 0..2", fg='red'))
            continue

        while True:
            try:
                n = int(input(style("\n(0) Wyjscie\n"
                                    "(1) Znajdź cykl Hamiltona\n"
                                    "(2) Znajdź cykl Eulera\n"
                                    "(3) Wyświetl w postaci listy następników\n"
                                    "(4) Wyświetl w postaci tabeli krawędzi\n"
                                    "(5) Wyświetl w postaci macierzy sąsiedztwa\n", fg='black', bold=True) +
                              "    Wybierz dzialanie [0/1/2/3/4/5] -> "))
            except ValueError:
                print(style("[!] Nalezy podac liczbe z zakresu 0..5", fg='red'))
                continue

            if n == 0:
                break
            elif n == 1:
                print(style("\nCykl Hamiltona", fg='blue'))
                print(hamilton(deepcopy(matrix)))
            elif n == 2:
                print(style("\nCykl Eulera", fg='blue'))
                print(euler(deepcopy(matrix)))
            elif n == 3:
                successors_list = lista_nastepnikow(deepcopy(matrix))
            elif n == 4:
                print("Tabela krawedzi?")
                edge_table = tabela_krawedzi(deepcopy(matrix))
            elif n == 5:
                macierz_sasiedztwa(deepcopy(matrix))
            else:
                print("Nalezy podac liczbe 0-5.")
                continue


if __name__ == '__main__':
    main(1)
