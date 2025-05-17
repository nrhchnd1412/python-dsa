def merge_dict(d1,d2):
    result = d1.copy()
    for k,v in d2.items():
        result[k]=result.get(k,0)+v
    return result

d1 = {'a': 1, 'b': 2, 'c': 3}
d2= {'b': 3, 'c': 4, 'd': 5}
r = merge_dict(d1,d2)

print(r)
