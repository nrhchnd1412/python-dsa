'''
🧠 Problem Statement
Place N queens on an NxN chessboard such that:

No two queens attack each other.
This means: no two queens can be on the same row, column, or diagonal.

Time: O(N!)
Space: O(N^2)
'''

def solve_n_queens(n):
    def backtrack(row):
        if row==n:
            board_copy=[''.join(r) for r in board]
            solutions.append(board_copy)
            return
        for col in range(n):
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue # not safe
            board[row][col]='Q'
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)

            backtrack(row+1)

            #backtrack
            board[row][col]='.'
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)

    solutions=[]
    board=[['.']*(n) for _ in range(n)]
    cols=set()
    diag1=set() # row-col
    diag2=set() # row+col
    backtrack(0)
    return solutions

print(solve_n_queens(4))
for solution in solve_n_queens(4):
    for row in solution:
        print(row)
    print()