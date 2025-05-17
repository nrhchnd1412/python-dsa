def recursive_range(num):
    if num in [0,1]:
        return num
    return num + recursive_range(num-1)

print(recursive_range(5))