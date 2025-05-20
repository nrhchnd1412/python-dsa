def merge_sort(my_arr):
    arr_length= len(my_arr)
    if arr_length<=1:
        return my_arr
    mid=arr_length//2
    left_half=my_arr[:mid]
    right_half=my_arr[mid:]
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)
    return merge(left_half,right_half)

def merge(left,right):
    i=j=0
    results=[]
    while i<len(left) and j <len(right):
        if left[i]<=right[j]:
            results.append(left[i])
            i+=1
        else:
            results.append(right[j])
            j+=1
    results.extend(left[i:])
    results.extend(right[j:])
    return results

my_arr=[6,1,-5,4,3,2,1,0.9876,-2]
result=merge_sort(my_arr)
print(result)