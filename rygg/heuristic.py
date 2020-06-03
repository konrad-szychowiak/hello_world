def heuristic(capacity, items):
    sol = []
    _size = 0
    _value = 0

    while _size < capacity and items:
        taken = items.pop()
        _size += taken.size
        sol.append(taken)

    sol.pop()

    [print(item) for item in sol]
    print(
        f"size: {sum([i.size for i in sol])}\nvalue:{sum([i.value for i in sol])}")
