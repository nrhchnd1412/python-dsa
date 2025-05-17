def is_odd(num):
    return num%2!=0

def recursive_with_callback(arr,callback):
    if len(arr)==0:
        return False
    return callback(arr[0]) or recursive_with_callback(arr[1:],callback)

print(recursive_with_callback([1,3,5],is_odd))