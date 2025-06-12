'''
Given:

N = target sum
nums[] = list of positive integers (e.g. [1, 2, 3])
Find the number of ways to reach sum N using elements of nums[], with unlimited supply of each element and order doesn't matter.
'''

def count_ways_to_sum(N,nums):
    dp=[0]*(N+1)
    dp[0]=1
    for num in nums:
        for i in range(num,N+1):
            dp[i]+=dp[i-num]
    return dp[N]

N = 4
nums = [1, 2, 3]
print(count_ways_to_sum(N, nums)) 