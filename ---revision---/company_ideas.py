'''
🔗 LeetCode 2306. Naming a Company

Problem Summary:
You are given an array of strings ideas where each string represents an idea. 
You want to name a company using two different ideas by swapping their first letters, and if the new words formed do not exist in the original list, then the pair is valid.

You need to return the number of valid company names formed like this.

Key Constraints:
All strings are distinct
1 <= ideas.length <= 10^5
1 <= ideas[i].length <= 10
All ideas are lowercase English letters

'''

from collections import defaultdict

def company_names(ideas):
    '''
    N = number of ideas
    M = average word length
    Time:O(N * M)
    Space: O(1)
    '''
    suffix_map=defaultdict(set)

    for idea in ideas:
        prefix=idea[0]
        suffix=idea[1:]
        suffix_map[prefix].add(suffix)
    total=0
    for i in range(26):
        for j in range(i+1,26):
            ch1=chr(ord('a')+i)
            ch2=chr(ord('a')+j)
            if ch1 in suffix_map and ch2 in suffix_map:
                # common suffix
                common = suffix_map[ch1] & suffix_map[ch2]
                count1 = len(suffix_map[ch1]-common)
                count2 = len(suffix_map[ch2]-common)
                total+=count1 * count2
    return total*2


print(company_names(["coffee", "donuts", "time", "toffee"])) # output 6