'''
Given an array nums consisting of n integers and an integer k,
find the maximum average value of any contiguous subarray of length k.

# Time : O(n)
# Space: O(1)
'''

def findMaxAverage(nums,window_size):
    if len(nums)<window_size:
        return -1
    total_sum=max_sum=sum(nums[:window_size])
    for i in range(window_size,len(nums)):
        total_sum+=nums[i]-nums[i-window_size]
        max_sum=max(max_sum,total_sum)
    return max_sum/window_size

print(findMaxAverage([1,12,-5,-6,50,3], 4))  # 12.75
print(findMaxAverage([5], 1))               # 5.0
print(findMaxAverage([-1,-12,-5,-6,-50,-3], 2))  # -5.5
