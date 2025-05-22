'''
Naive: O(n*k)
'''

def max_sum_subarray_naive(arr,k):
    max_sum=float('-inf')
    for i in range(len(arr)-k+1):
        current_sum= sum(arr[i:i+k])
        max_sum=max(max_sum,current_sum)
    return max_sum

'''
sliding window: O(n)
'''

def max_sum_subarray_sliding_window(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum+=arr[i]-arr[i-k]
        max_sum=max(max_sum,window_sum)
    return max_sum

print(max_sum_subarray_naive([1,2,10,4,5,6],3))
print(max_sum_subarray_sliding_window([1,2,10,4,5,6],3))