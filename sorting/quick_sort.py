def partition(arr, low, high):
    """
    Partition the array around a pivot element.
    All elements less than the pivot will be moved to the left,
    and all elements greater than the pivot to the right.
    
    Returns the final position of the pivot element.
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=None, high=None):
    """
    The main quick sort function that recursively sorts the array.
    
    Parameters:
    - arr: The array to be sorted
    - low: Starting index of the array (optional)
    - high: Ending index of the array (optional)
    """
    # Initialize default values on first call
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Find the partition index
        pivot_idx = partition(arr, low, high)
        
        # Sort elements before and after partition
        quick_sort(arr, low, pivot_idx - 1)  # Left side of pivot
        quick_sort(arr, pivot_idx + 1, high)  # Right side of pivot
    
    return arr