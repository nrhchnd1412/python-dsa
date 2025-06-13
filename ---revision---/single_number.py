'''
You are given an array of integers where:

Every number appears exactly 3 times, except one number which appears only once.
You must return that unique number.
Constraint: Solution must be in O(n) time and O(1) space.
'''
from collections import defaultdict, Counter

def single_number(nums):
    '''
    Although the time is linear, the space is not constant, 
    which violates the space constraint of the problem.
    '''
    d=defaultdict(int)
    for item in nums:
        d[item]=d[item]+1
    for k,v in d.items():
        if v==1:
            return k
        
def single_number_counter(nums):
    '''
    Although the time is linear, the space is not constant, 
    which violates the space constraint of the problem.
    '''
    counter=Counter(nums)
    for k,v in counter.items():
        if v==1:
            return k
        
def single_number_with_constraint(nums):
    result=0
    for i in range(32):
        bit_sum=0
        for num in nums:
            bit_sum+=(num>>i)&1
        if bit_sum%3!=0:
            result|=(1<<i)
    #handling 32 bit signed numbers
    if result>=2**31:
        result-=2**32
    return result

        
print(single_number([1,1,1,2,3,3,3,4,4]))
print(single_number_counter([1,1,1,2,3,3,3,4,4]))
print(single_number_with_constraint([1,1,1,2,3,3,3,4,4,4]))