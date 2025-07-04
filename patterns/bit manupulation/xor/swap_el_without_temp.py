'''
Swap two vars without using temp


Time: O(1)
Space:O(1)
'''

def swap_elements_without_temp(a,b):
    a=a^b
    b=a^b
    a=b^a
    return a,b

print(swap_elements_without_temp(2,3))