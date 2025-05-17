def power_of_two(n:int):
    if n<1:
        return 1
    power = power_of_two(n-1)
    return power*2

res=power_of_two(3)
print(res)
