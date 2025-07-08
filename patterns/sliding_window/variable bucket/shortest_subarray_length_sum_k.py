'''
📌 Leetcode 862: Shortest Subarray with Sum at Least K

Given an array of integers nums and an integer K, return the length of the shortest subarray 
such that the sum ≥ K.
If no such subarray exists, return -1.

Time: O(n)
Space: O(n)
'''

from collections import deque

def shortest_subarray(arr,k):
    n=len(arr)
    prefix= [0]*(n+1)
    for i in range (n):
        prefix[i+1]=prefix[i]+arr[i]
    
    dq=deque()
    min_length=float('inf')
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

'''
📌 WHY We Remove from the Back:
Suppose:

prefix[i] = 10
prefix[dq[-1]] = 12
And i > dq[-1] (since we're going left to right)

Now, any future prefix prefix[j] (where j > i) will try to subtract a prefix from the deque to check:

prefix[j] - prefix[?] ≥ K
Now between prefix[i] = 10 and prefix[dq[-1]] = 12, which is better to keep?

prefix[i] is smaller and occurs later.
Since we want prefix[j] - prefix[?] ≥ K to be easier, a smaller prefix[?] is better.
Also, we always want the latest, smallest value — smaller prefix gives larger subarray sum, and later index gives shorter subarray (if possible).
So:

prefix[dq[-1]] = 12 will never help find a better (shorter) valid subarray than prefix[i] = 10
Hence we remove dq[-1] from the deque — it's now useless
'''