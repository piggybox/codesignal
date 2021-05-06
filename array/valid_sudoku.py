def sudoku2(grid):
    n = len(grid)

    def has_dup(list):
        hash = {}

        for i in list:
            if i != '.':
                if i in hash:
                    return True
                else:
                    hash[i] = True

        return False

    # check rows
    for i in grid:
        if has_dup(i):
            return False

    # check columns
    for i in range(n):
        col = []
        for j in range(n):
            col.append(grid[j][i])

        if has_dup(col):
            return False

    # check blocks
    indexb = [0, 3, 6]
    index = [0, 1, 2]

    for row in indexb:
        for col in indexb:
            block = []

            for i in index:
                for j in index:
                    block.append(grid[row + i][col + j])

            if has_dup(block):
                return False

    return True