'''
Input: [[1,2,3],[4,5,6],[7,8,9]]
ouput: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
Time complexity: O(n^2)
'''

def rotate(m):
    n = len(m)
    c= len(m[0])
    # transpose the matrix
    for i in range(n):
        for j in range(i,n):
            m[i][j],m[j][i]=m[j][i],m[i][j]
    # reverse
    for i in range(n):
        left = 0
        right = c-1
        while(left<right):
            m[i][left], m[i][right]=m[i][right],m[i][left]
            left+=1
            right-=1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
rotate(matrix)
print(matrix)