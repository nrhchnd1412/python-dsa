import heapq

def heap_sort(my_arr):
    arr=my_arr.copy()
    heapq.heapify(arr)
    return [ heapq.heappop(arr) for _ in range(len(arr))]

def heap_sort_descending(my_arr):
    arr=[-v for v in my_arr]
    heapq.heapify(arr)
    return [ -heapq.heappop(arr) for _ in range(len(arr))]

my_arr=[6,1,-5,4,3,2,1,0.9876,-2]
result=heap_sort_descending(my_arr)
print(result)
print('hello')

print(heapq.nsmallest(2,my_arr))