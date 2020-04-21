
def Solve(grid):

    locate = FindEmptyLocation(grid)
    if locate:
        row, col = locate
    else:
        return True
    for i in range(1, 10):
        if isSafe(grid, row, col, i):
            grid[row][col] = i
            if Solve(grid):
                return True
            grid[row][col] = 0
    return False


def FindEmptyLocation(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def isSafeRow(grid, row, x):
    for i in range(9):
        if grid[row][i] == x:
            return False
    return True


def isSafeCol(grid, col, x):
    for i in range(9):
        if grid[i][col] == x:
            return False
    return True


def isSafeBox(grid, row, col, x):
    r = row - (row % 3)
    c = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if grid[i + r][j + c] == x:
                return False
    return True


def isSafe(grid, row, col, x):
    if isSafeRow(grid, row, x) and isSafeCol(grid, col, x) and isSafeBox(grid, row, col, x):
        return True
    return False



