'''
Given an array of non-negative integers arr and a start index, 
determine if you can reach any index with value 0.
From index i, you can jump either to i + arr[i] or i - arr[i].
'''
from collections import deque

def can_reach_index_with_zero(arr,start=0):
    visited=set()
    q=deque([start])
    while q:
        i = q.popleft()
        if arr[i]==0:
            return True
        if i in visited:
            continue
        visited.add(i)
        for next_i in [i+arr[i],i-arr[i]]:
            if 0<=next_i<len(arr):
                q.append(next_i)
    return False

def can_reach_index_with_zero_dfs(arr,start=0):
    def dfs(i):
        if i<0 or i >=len(arr) or arr[i]<0:
            return False
        if arr[i]==0:
            return True
        jump=arr[i]
        arr[i]=-arr[i]
        return dfs(i+jump) or dfs(i-jump)
    return dfs(start)



print(can_reach_index_with_zero([4,2,3,0,3,1,2], start = 5))
print(can_reach_index_with_zero([3,0,2,1,2], 2))

print(can_reach_index_with_zero_dfs([4,2,3,0,3,1,2], start = 5))
print(can_reach_index_with_zero_dfs([3,0,2,1,2], start=2))
