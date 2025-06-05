'''
You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.

O(nlogn) -- This uses Python’s built-in sorted() function, which is implemented using Timsort, a hybrid sorting algorithm
derived from merge sort and insertion sort.
'''

# Time complexity: O(nlogn)

def activity_selection(start,end):
    activities = sorted(zip(start,end),key=lambda x: x[1])
    last_end_time=0
    result =[]
    for s,e in activities:
        if s>=last_end_time:
            result.append((s,e))
            last_end_time=e
    return result

# Example
start_times = [1, 3, 0, 5, 8, 5]
end_times   = [2, 4, 6, 7, 9, 9]

selected = activity_selection(start_times, end_times)
print("Selected Activities (start, end):", selected)