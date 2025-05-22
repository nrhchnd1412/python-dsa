'''
Binary search with variations
'''
def iterative_binary_search(my_arr,target):
    left = 0
    right= len(my_arr)-1

    while left<=right:
        mid = left+(right-left)//2
        if my_arr[mid]==target:
            return mid
        elif my_arr[mid]<target:
            left = mid+1
        else:
            right=mid-1
    return -1

def iterative_binary_search_leftmost_occurence(my_arr,target):
    left = 0
    right= len(my_arr)-1
    found_index=-1
    while left<=right:
        mid = left+(right-left)//2
        if my_arr[mid]==target:
            found_index=mid
            right=mid-1
        elif my_arr[mid]<target:
            left = mid+1
        else:
            right=mid-1
    return found_index

def iterative_binary_search_rightmost_occurence(my_arr,target):
    left = 0
    right= len(my_arr)-1
    found_index=-1
    while left<=right:
        mid = left+(right-left)//2
        if my_arr[mid]==target:
            found_index=mid
            left=mid+1
        elif my_arr[mid]<target:
            left = mid+1
        else:
            right=mid-1
    return found_index

def recursive_binary_search(my_arr,target,left=0,right=None):
    if right is None:
        right = len(my_arr)-1
    if left>right:
        return -1
    mid = left + (right-left)//2 # avoid integer overflow
    if my_arr[mid]==target:
        return mid
    elif my_arr[mid]<target:
        return recursive_binary_search(my_arr,target,mid+1,right)
    else:
        return recursive_binary_search(my_arr,target,left,mid-1)

def find_insertion_point_before_duplicates(my_arr,target):
    left =0
    right = len(my_arr)-1
    while left<=right:
        mid = left +(right-left)//2
        if my_arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left

def find_insertion_point_after_duplicates(my_arr,target):
    left =0
    right = len(my_arr)-1
    while left<=right:
        mid = left +(right-left)//2
        if my_arr[mid]<=target:
            left=mid+1
        else:
            right=mid-1
    return left

my_arr=[1,3,3,3,4,4,4,4,4,8,9,10,34]
print(recursive_binary_search(my_arr,4))
print(iterative_binary_search(my_arr,4))
print(iterative_binary_search_leftmost_occurence(my_arr,4))
print(iterative_binary_search_rightmost_occurence(my_arr,4))
print(find_insertion_point_before_duplicates(my_arr,3))
print(find_insertion_point_after_duplicates(my_arr,3))