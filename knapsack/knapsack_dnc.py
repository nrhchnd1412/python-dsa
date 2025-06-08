'''
Knapsack solution using divide and conquer

Time complexitt: O(2^n)
'''

def knapsack(i,w):
    if i==0 or w==0:
        return 0
    if weights[i-1]>w:
        return knapsack(i-1,w)
    return max(
        values[i-1]+knapsack(i-1,w-weights[i-1]),
        knapsack(i-1,w)
    )

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)

print(knapsack(n,capacity))
