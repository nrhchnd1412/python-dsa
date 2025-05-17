def max_value_key(d):
    if not d:
        return None
    return max(d,d.get)

d1 = {'a': 1, 'b': 2, 'c': 3}
print(max(d1))