'''
Given an array of integers, find the length of the longest subsequence such that all elements of the subsequence are sorted in increasing order.

Note: A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

'''

def lis(nums):
    #Time: O(n^2)
    #space: O(n)
    n=len(nums)
    if n==0:
        return 0
    dp=[1]*n # each element is a LIS of 1

    for i in range(1,n):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i],1+dp[j])
    return max(dp)

def lis_optimized_using_binary_search(nums):
    pass

print(lis([3, 10, 2, 1, 20])) #output: 3
