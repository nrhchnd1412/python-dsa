'''
Problem:
Given an array of distinct integers candidates and a target, return all unique combinations of
candidates where the chosen numbers sum to target. You may reuse each number unlimited times.

Constraints:

All numbers are distinct
Reuse allowed

Time: O(N^T) where N = number of candidates
    T = target / smallest candidate

Space: O(T + output size)
'''

def unique_combinations_with_reuse(candidates,target):
    
    def backtrack(start,path,total):
        if total==target:
            result.append(path[:])
            return
        if total>target:
            return
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtrack(i,path,total+candidates[i])
            path.pop()
    result=[]
    backtrack(0,[],0)
    return result

print(unique_combinations_with_reuse([2, 3, 6, 7],7))
#output [[2, 2, 3], [7]]