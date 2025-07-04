'''
Given an array nums of integers (which can include negative numbers),
find the maximum sum of a contiguous subarray.
Return the sum only, not the subarray itself.

Time: O(n)
Space: O(1)
'''

def max_sum_contiguous_array(nums):
    max_sum=current_sum=nums[0]
    start=end=0
    for i in range(1,len(nums)):
        current_sum=max(nums[i],current_sum+nums[i])
        max_sum=max(max_sum,current_sum)
    return max_sum

def max_sum_contiguous_array_with_subarray(nums):
    max_sum=current_sum=nums[0]
    start=end=temp_start=0
    for i in range(1,len(nums)):
        if nums[i]>current_sum+nums[i]:
            current_sum=nums[i]
            temp_start=i
        else:
            current_sum+=nums[i]
        
        if current_sum > max_sum:
            start=temp_start
            end=i
            max_sum=current_sum
    return max_sum,nums[start:end+1]

print(max_sum_contiguous_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
print(max_sum_contiguous_array_with_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # (6, [4, -1, 2, 1])