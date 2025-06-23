'''
You're given a list of pairs:
Each pair is of the form (a, b) where a < b.
One pair (c, d) can follow another (a, b) if b < c.
You have to find the longest chain of such pairs.

Time: O(nlogn)
Space: O(1)
'''

def max_chain_length(pairs):
    pairs.sort(key=lambda x: x[1])
    current_end=float('-inf')
    count=0
    for a,b in pairs:
        if a>current_end:
            count+=1
            current_end=b
    return count

print(max_chain_length([[5, 24], [39, 60], [15, 28], [27, 40], [50, 90]])) #output: 3