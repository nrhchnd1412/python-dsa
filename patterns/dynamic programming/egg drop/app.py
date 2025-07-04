'''
The following is a description of the instance of this famous puzzle involving N=2 eggs and a building with H=36 floors:
Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:
An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If an egg breaks when dropped, then it would break if dropped from a higher window.
If an egg survives a fall, then it would survive a shorter fall.
It is not ruled out that the first-floor windows break eggs, nor is it ruled out that eggs can survive the 36th-floor windows.
If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only one way. Drop the egg from the first-floor window; if it survives, drop it from the second-floor window. Continue upward until it breaks. 
In the worst case, this method may require 36 droppings. Suppose 2 eggs are available. What is the lowest number of egg-droppings that is guaranteed to work in all cases?

Time: O(n * k²)
Space: O(n * k)
'''
import sys

def egg_drop(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][0]=0
        dp[i][1]=1
    for j in range(1,k+1):
        dp[1][j]=j # Only one egg, try all floors
    
    for eggs in range(2,n+1):
        for floors in range(2,k+1):
            dp[eggs][floors]=sys.maxsize
            for x in range(1,floors+1):
                res=1+max(dp[eggs-1][x-1],dp[eggs][floors-x])
                dp[eggs][floors]=min(dp[eggs][floors],res)
    return dp[n][k]

print(egg_drop(2,36)) # output : 8