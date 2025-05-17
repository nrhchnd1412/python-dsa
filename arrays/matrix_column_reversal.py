def reverse_columns_matrix(m):
    col= len(m[0])
    row = len(m)
    for i in range(col):
        top = 0
        bottom=row-1
        while(top<bottom):
            m[top][i],m[bottom][i]=m[bottom][i],m[top][i]
            top+=1
            bottom-=1


m= [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
reverse_columns_matrix(m)
print(m)