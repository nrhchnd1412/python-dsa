'''
📌 Problem Statement:

Given an array nums of distinct integers, return all the possible permutations of the array.

'''

def permutations(nums):
    # Time Complexity: O(n! *n) — Total permutations of n distinct elements (including output) else O(n!)
    # Space Complexity: O(n! * n)-- including output else O(n)
    def backtrack(path,used):
        if len(path)==len(nums):
            results.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i]=True
            path.append(nums[i])
            backtrack(path,used)

            used[i]=False
            path.pop()
    results=[]
    used=[False]* len(nums)
    backtrack([],used)
    return results

def permutations_with_duplicates(nums):
    '''
    Time Complexity: O(n! * n) in the worst case.
    Space Complexity: O(n) for recursion and used array.
    '''
    def backtrack(path,used):
        if len(path)==len(nums):
            results.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i >0 and nums[i]==nums[i-1] and not used[i-1]:
                continue
            used[i]=True
            path.append(nums[i])
            backtrack(path,used)

            used[i]=False
            path.pop()
    results=[]
    nums.sort()
    used=[False]* len(nums)
    backtrack([],used)
    return results

print(permutations([1,2,3])) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(permutations_with_duplicates([1,1,2])) # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]