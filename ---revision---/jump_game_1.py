'''
You are given an array of non-negative integers nums, where each element represents your maximum jump length at that position.
Question: Can you reach the last index starting from the first index?
'''

def can_jump(arr):
    max_reach=0
    for i, jump in enumerate(arr):
        if i> max_reach:
            return False
        max_reach=max(max_reach,i+jump)
    return True

print(can_jump([2, 3, 1, 1, 4]))
print(can_jump([3, 2, 1, 0, 4]))