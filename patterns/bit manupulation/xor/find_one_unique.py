'''
Given a list of integers, where:

All numbers appear exactly twice, except for 1 number, which appear only once,
Find the unique no in O(n) time and O(1) space.
'''

def find_unique(nums):
    '''
    Time: O(n)
    Space: O(1)
    '''
    result=0
    for num in nums:
        result^=num
    return result

print(find_unique([1,2,4,2,1])) # output: 4