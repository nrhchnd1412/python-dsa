'''
Input: [5,4,1,3,2], target = 6
Ouput: ((0,2), (1,4))
Time complexity: O(n)
'''

def target_sum_all_combinations(arr,target):
    track = {}
    result = tuple()
    for idx, num in enumerate(arr):
        diff = target - num
        if diff in track:
            result = result + ((track[diff],idx),)
        track[num]=idx
    return result

r = target_sum_all_combinations([5,4,1,3,2],6)
print(r)
