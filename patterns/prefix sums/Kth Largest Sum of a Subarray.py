'''
Given an integer array nums of size n and an integer k,
find the k-th largest sum of any non-empty contiguous subarray of nums.

Time: O(n² * logk)
    For each of the O(n²) subarray sums:
    Push into heap → O(logk)
    Possibly pop smallest → O(logk)

Space: O(n + k)
    Size = n + 1 → O(n)
    At most k elements → O(k)
'''
import heapq

def kth_largest_subarray_sum(nums,k):
    n=len(nums)
    prefix=[0]*(n +1)

    # sum of first i elements
    for i in range(n):
        prefix[i+1]=prefix[i]+nums[i]
    min_heap=[]
    for i in range(n):
        for j in range(i+1,n+1):
            _sum=prefix[j]-prefix[i]
            heapq.heappush(min_heap,_sum)
            if len(min_heap)>k:
                # maintain only top k largest elements in heap
                # out of which, first element is kth largest
                heapq.heappop(min_heap)
    return min_heap[0]

print(kth_largest_subarray_sum([2, -1, 3],2)) # 3
    