# Time Complexity: O(n^2)
# O(n x n/2) -- inner while loop runs around n/2 times

def reverse_matrix_row(matrix):
    n = len(matrix)
    c= len(m[0])
    for i in range(n):
        left =0
        right = c-1
        while(left<right):
            matrix[i][left], matrix[i][right]= matrix[i][right],matrix[i][left]
            left+=1
            right-=1

m = [[1,2,3],[4,5,6],[7,8,9]]
reverse_matrix_row(m)
print(m)