'''
At any point, we just need prev and current row.
We can optimize space to O(n)

Time: O(m*n)
Space: O(n)
'''

def space_optimized_min_cost_path(costs):
    col=len(costs[0])
    rows=len(costs)
    prev=[0]*col
    prev[0]=cost[0][0]
    current=[0]*col

    # fill prev
    for j in range(1,col):
        prev[j]=costs[0][j]+prev[j-1]
    
    for i in range(1,rows):
        current[0]=prev[0]+costs[i][0]
        for j in range(1,col):
            current[j]=costs[i][j]+min(
                prev[j],
                current[j-1],
                prev[j-1]
            )
        prev,current=current,prev
    return prev[col-1]

cost = [
    [1, 3, 5],
    [2, 1, 2],
    [4, 3, 1]
]
print(space_optimized_min_cost_path(cost))  # Output: 3