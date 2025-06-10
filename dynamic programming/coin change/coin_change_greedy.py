'''
You are given:

A list of coin denominations: coins = [1, 2, 5]
A total amount: amount = 11
Goal: Find the minimum number of coins required to make up that amount.

If it's not possible, return -1.
'''

def coin_change_greedy(coins,amt):
    coins.sort(reverse=True)
    result=0
    for coin in coins:
        if amt>=coin:
            n = amt//coin
            result+=n
            amt-=n*coin
    if amt!=0:
        return -1
    return result

print(coin_change_greedy([1, 2, 5], 11))   # Output: 3 (5 + 5 + 1)
print(coin_change_greedy([1, 3, 4], 6))    # Output: 3 ❌ (not optimal)