'''
[LC 3]
🔶 Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Time : O(n)
Space: O(min(n,m))
'''

def max_length_non_repeating_chars(s):
    left=max_length=0
    chars={}
    for right in range(len(s)):
        if s[right] in chars and chars[s[right]]>=left:
            left=chars[s[right]]+1
        chars[s[right]]=right
        max_length=max(max_length,right-left+1)
    return max_length

print(max_length_non_repeating_chars("abcabcbb")) #3
print(max_length_non_repeating_chars("bbbb")) #1
print(max_length_non_repeating_chars("pwwkew")) #3