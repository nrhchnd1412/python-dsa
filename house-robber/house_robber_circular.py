'''
Problem:
Houses are arranged in a circle, meaning the first and last houses are adjacent.
You still can’t rob two adjacent houses, including the first and last together.
Goal: Maximize the total money robbed.
'''

def house_robber_circular(nums):
    n=len(nums)
    if n==0:
        return 0
    if n==1:
        return nums[0]
    
    def linear(nums):
        p1,p2=0,0
        for num in nums:
            temp=p1
            p1=max(p2+num,p1)
            p2=temp
        return p1
    return max(linear(nums[:-1]),linear(nums[1:]))

nums = [2, 3, 2]
print(house_robber_circular(nums))