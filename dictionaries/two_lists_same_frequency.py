
def check_same_frequency(list1, list2):
    def counter(lst):
        result = {}
        for num in lst:
            result[num]=result.get(num,0)+1
        return result
    return counter(list1)==counter(list2)