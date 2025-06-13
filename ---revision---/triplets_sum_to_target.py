'''
Find All Triplets (3-Sum)
Time: O(n^2)
Space: O(1)
'''

def find_triplets(items,target):
    result =[]
    items.sort()
    n=len(items)
    for i in range(n-2):
        if i>0 and items[i]==items[i-1]:
            continue
        left,right=i+1,n-1
        while left<right:
            total = items[i]+items[left]+items[right]
            if total==target:
                result.append((items[i],items[left],items[right]))
                while left<right and items[left]==items[left+1]:
                    left+=1
                while left<right and items[right]==items[right-1]:
                    right-=1
                left+=1
                right-=1
            elif target<total:
                right-=1
            else:
                left+=1
    return result

print(find_triplets([-2, 0, 1, 1, 2],0)) #[(-2, 0, 2), (-2, 1, 1)]