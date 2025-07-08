'''
🔹 Problem Statement (LC 1004 – Max Consecutive Ones III)
Given:

Array nums consisting of 0s and 1s.
An integer k – the maximum number of 0s you can flip to 1s.
Goal:
Return the length of the longest subarray with at most k zeros flipped to 1s.

Time: O(n)
Space: O(1)
'''

def max_consecutive_ones(nums,k):
    left=max_length=zeros=0
    for right in range(len(nums)):
        if nums[right]==0:
            zeros+=1
        while zeros>k:
            if nums[left]==0:
                zeros-=1
            left+=1
        max_length=max(max_length,right-left+1)
    return max_length

print(max_consecutive_ones([1, 1, 0, 0, 1, 1, 1, 0],2)) # 7