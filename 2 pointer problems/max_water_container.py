'''
Given n non negative integers as vertical lines on chart,
find the max water area for the container created by any two lines.
'''

def max_water_area(my_arr):
    water_area=0
    if len(my_arr)<2:
        return 0
    left =0
    right =len(my_arr)-1
    while(left<right):
        current_length=min(my_arr[left],my_arr[right])
        width = right-left
        water_area = max(
            water_area,
            current_length * width
        )
        if my_arr[left]<my_arr[right]:
            left+=1
        else:
            right-=1
    return water_area

my_arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water_area(my_arr))
