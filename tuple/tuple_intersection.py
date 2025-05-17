'''
Time Complexity: O(n+m)
'''

def set_intersection(t1,t2):
    return tuple(set(t1)& set(t2))

print(
    set_intersection((1,2,3),(3,4,5,1))
)