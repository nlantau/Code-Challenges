# nlantau, 2021-02-01
import numpy as np


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

p = list()

def sudoku(puzzle):
    global p
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                for n in range(1,10):
                    if possible(puzzle,r,c,n):
                        puzzle[r][c] = n
                        sudoku(puzzle)
                        puzzle[r][c] = 0
                return
    p.append(puzzle)
    print(np.matrix(puzzle))
    return p


def possible(p,r,c,n):
    for i in range(0,9):
        if p[r][i] == n:
            return False
    for i in range(0,9):
        if p[i][c] == n:
            return False
    c0 = (c//3)*3
    r0 = (r//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if p[r0+i][c0+j] == n:
                return False
    return True




if __name__ == "__main__":
    print(np.matrix(puzzle))
    print(np.matrix(sudoku(puzzle)))
