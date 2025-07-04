'''
Given a list of integers, where:

All numbers appear exactly twice, except for two numbers, which appear only once,
Find those two unique numbers in O(n) time and O(1) space.
'''

def find_two_unique(nums):
    '''
    Time: O(n)
    Space: O(1)
    '''
    result =0
    for num in nums:
        result^=num
    
    set_bit=result & -result
    x=0
    y=0
    for num in nums:
        if num & set_bit:
            x^=num
        else:
            y^=num
    return x,y

print(find_two_unique([1,1,2,3,4,4]))