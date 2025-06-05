'''
You are given an array of non-negative integers nums, where each element represents your maximum jump length at that position.
Question: find the minimum jumps from first index needed to reach last index?
'''

# Greedy algorithm
def find_minimum_jumps(arr):
    n = len(arr)
    jumps=0
    current_end=0
    farthest=0
    for i in range(n-1):
        farthest = max(farthest,i+arr[i])
        if i == current_end:
            jumps+=1
            current_end=farthest
    return jumps

nums = [3,2,1,1,3,4]
print(find_minimum_jumps(nums))