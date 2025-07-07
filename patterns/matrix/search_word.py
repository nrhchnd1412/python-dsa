'''
Given a 2D matrix of characters, determine if a given word exists 
in the matrix by moving only right or down.

Time : O(m × n × 2^L)
Space: O(L)
'''

def word_exists(matrix,word):
    def dfs(i,j,idx):
        if idx==len(word):
            return True
        if i>=rows or j>=cols or matrix[i][j]!=word[idx]:
            return False
        return dfs(i,j+1,idx+1) or dfs(i+1,j,idx+1)
    rows=len(matrix)
    cols=len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==word[0] and dfs(i,j,0):
                return True
    return False

board = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]
word = "ABE"

print(word_exists(board,word))