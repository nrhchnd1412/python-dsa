def rain_water_trapping(arr):
    if not arr or len(arr)<3:
        return 0
    left=0
    right=len(arr)-1

    left_max = arr[left]
    right_max = arr[right]
    water_trapped =0
    while left<right:
        if arr[left]<=arr[right]:
            left+=1
            left_max = max(left_max,arr[left])
            water_trapped+=left_max-arr[left]
        else:
            right-=1
            right_max=max(right_max,arr[right])
            water_trapped+=right_max-arr[right]
    return water_trapped

arr =[4,0,3,1,4]
print(rain_water_trapping([4,0,3,1,4]))
print(rain_water_trapping([3,2,2]))
print(rain_water_trapping([1, 2, 3, 4]))
print(rain_water_trapping([5,0,2,0,4]))
print(rain_water_trapping([1,0,3,4,7,0,5,0,3]))
print(rain_water_trapping([3, 0, 1, 0, 4, 0, 2]))
                