'''
Find All Pairs That Sum to a Target
'''

def find_pairs(items,target):
    # Time : O(n)
    # space: O(n)
    seen=set()
    result=set()
    for item in items:
        complement= target-item
        if complement in seen:
            result.add(tuple(sorted((item,complement))))
        seen.add(item)
    return list(result)

def find_pairs_two_pointer(items,target):
    # Time: O(nlogn)
    # Space: O(1)
    left,right=0,len(items)-1
    result=[]
    items.sort()
    while left<right:
        total=items[left]+items[right]
        if total==target:
            result.append((items[left],items[right]))
            #skip duplicate values
            while left<right and items[left]==items[left+1]:
                left+=1
            while left<right and items[right]==items[right-1]:
                right-=1
            left+=1
            right-=1
        elif total<target:
            left+=1
        else:
            right-=1
    return result
    
print(find_pairs([1, 2, 3, 4, 5], 6))
print(find_pairs_two_pointer([1, 2, 3, 4, 5], 6) )
# Output: [(2, 4), (1, 5), (3, 3)]