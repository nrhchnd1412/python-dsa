'''
bubble sort
'''

def bubble_sort(my_arr):
    n= len(my_arr)
    for i in range(n):
        # after each pass, largest element is moved to extreme right
        swapped=False
        for j in range(n-i-1):
            if my_arr[j]>my_arr[j+1]:
                swapped=True
                my_arr[j],my_arr[j+1]=my_arr[j+1],my_arr[j]
        if not swapped:
            break

my_arr=[8,6,1,2,3,5,4,7]
bubble_sort(my_arr)
print(my_arr)