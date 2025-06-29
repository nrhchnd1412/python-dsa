'''
You're given an array arr of length n-2, containing distinct numbers from 1 to n.
Two numbers are missing, find them in O(n) time and O(1) space.
'''

def two_missing(nums,n):
    '''
    Time: O(1)
    Space: O(1)
    '''
    total_xor=0
    for i in range(1,n+1):
        total_xor^=i
    for num in nums:
        total_xor^=num

    set_bit=total_xor & -total_xor
    x=0
    y=0
    for i in range(1,n+1):
        if i & set_bit:
            x^=i
        else:
            y^=i
        
    for num in nums:
        if num & set_bit:
            x^=num
        else:
            y^=num
    
    return x,y


print(two_missing([1,2,4,6],6)) # output: (3,5)