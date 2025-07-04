'''
📌 Problem Statement:

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets, and the elements in a subset can be in any order.

Time Complexity: O(2ⁿ × n) (though runtime complexity is less due to duplicates being removed)
Space Complexity: O(2ⁿ * n) for storing all subsets
'''

def power_set(nums):
    def backtrack(start,path):
        results.append(path[:])
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
    results=[]
    nums.sort()
    backtrack(0,[])
    return results

nums=[1,2,2,3,3]
print(power_set(nums))