'''
You are given:

A list of coin denominations: coins = [1, 2, 5]
A total amount: amount = 11
Goal: Find the minimum number of coins required to make up that amount.

If it's not possible, return -1.
'''


def coin_change_dp(coins,amt):
    dp =[float("inf")]*(amt+1)
    dp[0]=0
    for coin in coins:
        for x in range(coin,amt+1):
            dp[x]=min(dp[x],dp[x-coin]+1)
    return dp[amt] if dp[amt]!=float("inf") else -1



print(coin_change_dp([1, 2, 5], 11))   # Output: 3 (5 + 5 + 1)
print(coin_change_dp([1, 3, 4], 6))    # Output: 2 