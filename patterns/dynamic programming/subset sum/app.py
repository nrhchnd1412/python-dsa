'''
Given a list of non-negative integers and a target sum,
we determine whether there exists a subset of the list that adds up to the target.

Time/Space: O(n*target)
'''

def subset_sum(arr,target):
    n=len(arr)
    dp=[[False]*(target+1) for _ in range(n+1)]
    # target = 0 for an empty subset
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,target+1):
            if j<arr[i-1]:
                dp[i][j]=dp[i-1][j] # dont include
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]] # exclude or include
    return dp[n][target]

print(subset_sum([3, 34, 4, 12, 5, 2],9))
print(subset_sum([3, 34, 4, 12, 5, 2],30))
