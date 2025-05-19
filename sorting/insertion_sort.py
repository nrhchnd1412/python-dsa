'''
Insertion sort
'''

def insertion_sort(my_arr):
    n = len(my_arr)
    for i in range(1,n):
        j=i-1 # previoud element
        current_element = my_arr[i]
        while j>=0 and current_element<my_arr[j]:
            my_arr[j+1]=my_arr[j]
            j-=1
        my_arr[j+1]=current_element

my_arr=[6,1,5,4,3,2]
insertion_sort(my_arr)
print(my_arr)
