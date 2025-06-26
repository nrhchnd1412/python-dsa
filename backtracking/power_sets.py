'''
Problem: Subsets (Power Set)
Given an array of distinct integers, return all possible subsets (the power set).

The solution must not contain duplicate subsets.
You can return the subsets in any order.

Time Complexity: O(2ⁿ × n)
Space Complexity: O(2ⁿ) for storing all subsets
'''

def powersets(nums):
    results=[]

    def backtrack(start,path):
        results.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
    backtrack(0,[])
    return results

print(powersets([1, 2, 3]))