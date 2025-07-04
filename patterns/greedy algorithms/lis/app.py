'''
We can use a greedy + binary search approach using bisect module.
'''


import bisect

def lis_optimized(nums):
    # Time: O(nlogn)
    subs=[]
    for num in nums:
        idx=bisect.bisect_left(subs,num)
        if idx==len(subs):
            subs.append(num)
        else:
            subs[idx]=num
    return len(subs)
    
print(lis_optimized([10, 9, 2, 5, 3, 7, 101, 18]))