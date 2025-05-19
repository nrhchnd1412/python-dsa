'''
selection sort
'''

def selection_sort(my_arr):
    n=len(my_arr)
    for i in range(n):
        mid_idex=i
        for j in range(i+1,n):
            if my_arr[j]<my_arr[mid_idex]:
                mid_idex=j
        my_arr[i],my_arr[mid_idex]=my_arr[mid_idex],my_arr[i]

my_arr=[8,6,1,2,3,5,4,7]
selection_sort(my_arr)
print(my_arr)