# Time complexity: O(n)
def contains_duplicate(nums):
    if len(set(nums)) < len(nums):
        return True
    return False
