'''
🔹 Problem Statement (LC 487 – Max Consecutive Ones II)
Given:

Array nums consisting of 0s and 1s.
Only one flip of 0 to 1 is allowed
Goal:
Return the length of the longest subarray with at most one zero flipped to 1

Time: O(n)
Space: O(1)
'''

def max_consecutive_ones(nums):
    left=max_length=zeros=0
    for right in range(len(nums)):
        if nums[right]==0:
            zeros+=1
        while zeros>1:
            if nums[left]==0:
                zeros-=1
            left+=1

        max_length=max(max_length,right-left+1)
    return max_length

print(max_consecutive_ones([1, 1, 0, 0, 1, 1, 1, 0])) # 4