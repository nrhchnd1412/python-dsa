'''
Given:

A set of items, each with:
value[i]: value of the item
weight[i]: weight of the item
A maximum weight capacity W of the knapsack
Goal:

Maximize the total value in the knapsack

O(nlogn) -- sorting
'''

class Item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight

def find_max_knapsack_value(items,capacity):
    total_value=0.0
    items.sort(key = lambda x:x.value/x.weight,reverse=True)
    for item in items:
        if capacity>=item.weight:
            total_value+=item.value
            capacity-=item.weight
        else:
            fraction=capacity/item.weight
            total_value+=item.value * fraction
            break
    return total_value


items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]
capacity = 50

print(f"Maximum value in knapsack: {find_max_knapsack_value(items,capacity)}")