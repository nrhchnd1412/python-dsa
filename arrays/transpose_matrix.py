# Time Complexity: O(n^2)


def transpose(matrix):
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


m = [[1,2,3],[4,5,6],[7,8,9]]
transpose(m)
print(m)