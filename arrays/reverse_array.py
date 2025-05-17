'''
Time complexity: O(n)...(n/2) for n elements but we ignore the constant factor.
'''

def reverse_array(arr):
    n = len(arr)
    left =0
    right = n-1
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1