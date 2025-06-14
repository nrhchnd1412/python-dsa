'''
Imagine a 2D grid (matrix) where each cell has a cost to step on. You start from the top-left corner (0,0) and want to reach the bottom-right corner. From any cell, you can usually move:

Right
Down

Your goal is to reach the last cell with minimum total cost.
'''

def min_cost_path(cost):
    # time, space = O(m*n)
    rows=len(cost)
    cols= len(cost[0])
    dp=[[0]*cols for _ in range(rows)]
    dp[0][0]=cost[0][0]
    # set first row
    for i in range(1,cols):
        dp[0][i]=dp[0][i-1]+cost[0][i]
    
    # set first column
    for i in range(1,rows):
        dp[i][0]=cost[i][0]+dp[i-1][0]
    
    # set rest of the table

    for i in range(1,rows):
        for j in range(1,cols):
            dp[i][j]=cost[i][j]+min(dp[i][j-1],dp[i-1][j])
    return dp[rows-1][cols-1]

def min_cost_path_with_diagonal(cost):
    # time, space = O(m*n)
    rows=len(cost)
    cols= len(cost[0])
    dp=[[0]*cols for _ in range(rows)]
    dp[0][0]=cost[0][0]
    # set first row
    for i in range(1,cols):
        dp[0][i]=dp[0][i-1]+cost[0][i]
    
    # set first column
    for i in range(1,rows):
        dp[i][0]=cost[i][0]+dp[i-1][0]
    
    # set rest of the table

    for i in range(1,rows):
        for j in range(1,cols):
            dp[i][j]=cost[i][j]+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[rows-1][cols-1]

def min_cost_path_with_diagonal_and_path(cost):
    rows=len(cost)
    cols=len(cost[0])
    dp=[[0]*cols for _ in range(rows)]
    parents=[[None]*cols for _ in range(rows)]
    dp[0][0]=cost[0][0]

    # set first row
    for j in range(1,cols):
        dp[0][j]=cost[0][j]+dp[0][j-1]
        parents[0][j]=(0,j-1)
    
    # set first col
    for i in range(1,rows):
        dp[i][0]=cost[i][0]+dp[i-1][0]
        parents[i][0]=(i-1,0)

    # set rest of dp table

    for i in range(1,rows):
        for j in range(1,cols):
            choices=[
                (dp[i][j-1],(i,j-1)),
                (dp[i-1][j],(i-1,j)),
                (dp[i-1][j-1],(i-1,j-1))
            ]
            min_value,prev_cell=min(choices,key=lambda x: x[0])
            dp[i][j]=min_value+cost[i][j]
            parents[i][j]=prev_cell
    i,j=rows-1,cols-1
    path=[]
    while True:
        path.append((i,j))
        if parents[i][j] is None:
            break
        i,j=parents[i][j]
    path.reverse()
    return dp[rows-1][cols-1],path

cost = [
    [1, 3, 5],
    [2, 1, 2],
    [4, 3, 1]
]
print(min_cost_path(cost))  # Output: 7
print(min_cost_path_with_diagonal(cost))  # Output: 7
print(min_cost_path_with_diagonal_and_path(cost))  # Output: 7