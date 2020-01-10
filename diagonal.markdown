# Diagonal sum in a matrix

1. Get number of rows (`N`) and columns (`M`)
    ```py
    N, M = input().split()
    N, M = int(N), int(M)
    # That could've be done with `map(..., input().split())` as well
    ```
1. Create first diagonal (`diag`) and antidiagonal (`adia`)
    ```py
    diag = list(map(lambda x: 0, range(M)))
    adia = list(map(lambda x: 0, range(M)))
    # OR: adia = diag.copy()
    ```
    
1. Read values from each row:
    ```py
    for _n in range(n):
        # get values in a row:
        line = input().split()
        for _m in range(m):
            # add to diag (first M indices)
            diag[_m] += int(line[_m])
            
            # add to adia (last M indices)
            adia[_m+_n] += int(line[_m])
        
        # add new diagonals and antidiagonal
        # at the end and the beginning of lists
        diag = [0] + diag
        adia = adia + [0]

    diag.sort()
    adia.sort()

1. Print the greatest value from either of `diag` or `adia`
    ```py
    print(   diag[-1] if diag[-1] > adia[-1] else adia[-1]   )
    ```
