def flatten_array(arr):
    result =[]
    for item in arr:
        if isinstance(item, list):
           result.extend(flatten_array(item))
        else:
            result.append(item)
    return result

print(flatten_array([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))