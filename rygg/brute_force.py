from rygg.classes import *


def dec_to_bin(x, n):
    return bin(x)[2:].zfill(n)


def weights_sum(binary, items):
    total = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            total += items[i].size
    return total


def value_sum(binary, items):
    total = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            total += items[i].value
    return total


def find_solution(binary):
    return [str(i) for i in range(len(binary)) if binary[i] == '1']


def brute_force(capacity, n, items):
    max_value = 0
    solution = ''
    for i in range(1, 2**n - 1):
        print('.', end="")
        binary = dec_to_bin(i, n)
        # print(binary)
        total_weight = weights_sum(binary, items)

        if total_weight <= capacity:
            total_value = value_sum(binary, items)
            if total_value > max_value:
                max_value = total_value
                solution = binary
        print()
    # result = find_solution(solution)
    # print('Lista elementow: {', ', '.join(result), '}')
    # print('Waga wybranych elementów: ', weights_sum(solution, items))
    # print('Wartosc wybranych elementów: ', value_sum(solution, items))
    # return result
    return solution
