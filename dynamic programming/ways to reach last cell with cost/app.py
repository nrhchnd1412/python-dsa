'''
Given a grid[i][j] where each cell has a cost, and a target_cost, 
count how many unique paths exist from the top-left (0,0) to the bottom-right (m-1, n-1)
such that the total cost is equal to target_cost.
You can only move right or down.

Time/Space : O(m * n * target_cost)
'''

def count_paths_with_cost(grid,target_cost):
    m=len(grid)
    n=len(grid[0])
    dp=[[[0]* (target_cost+1) for _ in range(n)] for _ in range(m)]
    if grid[0][0]<=target_cost:
        dp[0][0][grid[0][0]]=1
    for i in range(m):
        for j in range(n):
            for cost in range(1,target_cost+1):
                if cost-grid[i][j]<0:
                    continue
                ways=0
                if i>0:
                    #from top
                    ways+=dp[i-1][j][cost-grid[i][j]]
                if j>0:
                    #from left
                    ways+=dp[i][j-1][cost-grid[i][j]]
                dp[i][j][cost]+=ways
    return dp[m-1][n-1][target_cost]

grid = [
    [1, 2, 3],
    [4, 6, 5],
    [3, 2, 1]
]
target_cost = 12

print(count_paths_with_cost(grid, target_cost)) #output 2