'''
You are a thief trying to rob houses along a street. 
Each house has some money stored, but you can't rob two adjacent houses — if you do, an alarm will go off.

Your goal is to maximize the amount of money you can rob.
'''

def rob_house_dp(nums):
    # Time complexity: O(n)
    # Space complexity: O(n)
    n=len(nums)
    dp=[0]*n
    dp[0]=nums[0]
    dp[1]=nums[1]

    for i in range(2,n):
        dp[i]=max(dp[i-2]+nums[i],dp[i-1])
    return dp[-1]

def rob_house_space_optimized(nums):
    # Time complexity: O(n)
    # Space complexity: O(1)
    p1,p2=0,0
    for num in nums:
        temp=p1
        p1=max(p2+num,p1)
        p2=temp
    return p1

nums = [2, 7, 9, 3, 1]

print(rob_house_dp(nums)) # output 12
print(rob_house_space_optimized(nums))
