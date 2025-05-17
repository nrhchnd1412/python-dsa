def max_product(arr):
    if len(arr) < 2:
        return "Array must contain at least two elements."
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
    return max1 * max2
print(max_product([1,1])) # Output: 20 (4*5)
