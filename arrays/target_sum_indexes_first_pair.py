'''
Input: [1,2,3,4], target = 5
Ouput: 1,2
Time complexity: O(n)
'''

def target_sum(arr,target):
    result = {}
    for idx, num in enumerate(arr):
        diff = target - num
        if diff in result:
            return result[diff],idx
        result[num]=idx
    return None

r = target_sum([1,2,3,4],5)
print(r)
