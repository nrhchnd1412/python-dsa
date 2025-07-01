'''
Problem:
Given a collection of candidate numbers (with duplicates) and a target, 
find all unique combinations where each number can be used at most once.
The solution set must not contain duplicate combinations.

Constraints:

Duplicates present
Reuse NOT allowed
Output should have unique combinations (no duplicate sets)

Time: O(2^N)

Space: O(N + output size)
'''

def combination_without_reuse(candidates,target):
    def backtrack(start,path,total):
        if total==target:
            result.append(path[:])
            return
        if total>target:
            return
        for i in range(start,len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i+1,path,total+candidates[i])
            path.pop()

    candidates.sort()
    result=[]
    backtrack(0,[],0)
    return result

print(combination_without_reuse([10,1,2,7,6,1,5],8))
#output [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]