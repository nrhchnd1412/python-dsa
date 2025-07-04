'''
You're given an array arr of size n-1, which contains distinct integers from 1 to n, but one number is missing.

Example:
arr = [1, 2, 4, 5] → n = 5 → Missing = 3

'''
def missing_no_formula(nums,n):
    '''
    Time: O(n)
    Spce: O(1)
    '''
    sum_actual=n*(n+1)//2
    sum_case=sum(nums)
    return sum_actual-sum_case

def missing_no(nums,n):
    '''
    Time: O(n)
    Spce: O(1)
    '''
    result =0
    for i in range(1,n+1):
        result^=i
    for num in nums:
        result^=num
    return result

print(missing_no([1,2,3,5],5))
print(missing_no_formula([1,2,3,5],5))