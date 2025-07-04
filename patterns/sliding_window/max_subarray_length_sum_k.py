'''
Given an array of integers nums and an integer K, return the length of the shortest subarray 
such that the sum ≥ K.
If no such subarray exists, return -1.
'''

from collections import deque

def shortest_subarray(arr,k):
    n=len(arr)
    prefix= [0]*(n+1)
    for i in range (n):
        prefix[i+1]=prefix[i]+arr[i]
    
    dq=deque()
    min_length=n+1
    for i in range(n + 1):
        # Check if there's a valid subarray
        while dq and prefix[i] - prefix[dq[0]] >= k:
            min_length = min(min_length, i - dq.popleft())
        
        # Maintain increasing order of prefix sums in deque
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    return min_length if min_length <= n else -1

print(shortest_subarray([2, -1, 2], 3))   # Output: 3
print(shortest_subarray([1, 2], 4))       # Output: -1
print(shortest_subarray([1, 2, 3, 4, 5], 11))  # Output: 3

