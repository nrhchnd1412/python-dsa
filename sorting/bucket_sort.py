'''
bucket sort
'''

def insertion_sort(my_arr):
    n = len(my_arr)
    for i in range(1,n):
        current_element = my_arr[i]
        j=i-1
        while j>=0 and my_arr[j]> current_element:
            my_arr[j+1]=my_arr[j]
            j-=1
        my_arr[j+1]=current_element

def bucket_sort(my_arr,no_of_buckets=10):

    min_value=min(my_arr)
    max_value=max(my_arr)

    if max_value == min_value:
        return my_arr
    
    value_range = max_value-min_value
    bucket_range = value_range/no_of_buckets
    buckets =[[] for _ in range(no_of_buckets)]

    for num in my_arr:
        bucket_index= int((num-min_value)/bucket_range)
        if bucket_index==no_of_buckets:
            bucket_index=bucket_index-1
        buckets[bucket_index].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    result =[]
    for bucket in buckets:
        result.extend(bucket)
    return result

my_arr=[6,1,-5,4,3,2,1,0.9876,-2]
result=bucket_sort(my_arr)
print(result)