'''
Given:

A list of items, each with:
value[i]: profit/value of the item
weight[i]: weight of the item
A maximum weight W that the knapsack can carry
Goal:

Maximize total value, but you can either take an item or leave it — no partial/fractional items allowed.
'''

def knapsack_01(values,weights,capacity):
    n = len(values)
    dp =[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                #value if we include
                value_if_included = values[i-1]+dp[i-1][w-weights[i-1]]
                #value if excluded
                value_if_excluded= dp[i-1][w]
                dp[i][w]=max(value_if_included,value_if_excluded)
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][w]

# Test
values = [1, 2, 3]
weights = [4, 5, 1]
capacity= 4

print("Maximum value:", knapsack_01(values, weights, capacity)) # output: 3
print(knapsack_01([60, 100, 120], [10, 20, 30], 50))