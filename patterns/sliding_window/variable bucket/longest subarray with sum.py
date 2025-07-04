'''
Given an array of positive integers and a target sum T,
find the length of the longest subarray with sum ≤ T.

Time: O(n)
Space: O(1)

Below approach only works if numbers are all +ve
'''

def longest_subarray_with_sum(nums,target):
    left =0
    total_sum=0
    max_length=0
    for right in range(len(nums)):
        total_sum+=nums[right]
        while total_sum > target:
            total_sum-=nums[left]
            left+=1
        max_length=max(max_length,right-left+1)
    return max_length

print(longest_subarray_with_sum([1, 2, 1, 0, 1, 1, 0],4))