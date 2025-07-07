'''
Problem: Find the maximum sum of any subarray of fixed size k.
works with -ve numbers as well.
'''

def max_sum_subarray_sliding_window(arr,k):
    # Time: O(n)
    # Space: O(1)
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum+=arr[i]-arr[i-k]
        max_sum=max(max_sum,window_sum)
    return max_sum

print(max_sum_subarray_sliding_window([1,2,10,4,5,6],3)) #19