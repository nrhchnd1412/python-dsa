'''
Given an array of integers nums and an integer K, return the length of the shortest subarray 
such that the sum ≥ K.
If no such subarray exists, return -1.
'''

from collections import deque

def shortest_subarray(nums, K):
    n = len(nums)
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    
    dq = deque()
    min_len = float('inf')
    
    for j in range(len(prefix)):
        # Check if current prefix[j] - prefix[i] >= K
        while dq and prefix[j] - prefix[dq[0]] >= K:
            min_len = min(min_len, j - dq.popleft())
        
        # Maintain increasing order of prefix values in deque
        while dq and prefix[j] <= prefix[dq[-1]]:
            dq.pop()
        
        dq.append(j)
    
    return min_len if min_len != float('inf') else -1

x=[1,2,3,4,5,6,7]
print(shortest_subarray(x,9))