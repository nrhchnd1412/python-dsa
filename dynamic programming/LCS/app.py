'''
Given two sequences (usually strings) text1 and text2, find the length of their longest subsequence that appears in the same relative order, but not necessarily contiguous.

A subsequence is a sequence that appears in the same order but not necessarily contiguously.

Time/Space: O(m*n)
Space can be optmimized to O(1)
'''

def longest_common_subsequence(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[i-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

print(longest_common_subsequence("abcde", "ace"))  # Output: 3
print(longest_common_subsequence("abc", "def"))    # Output: 0
print(longest_common_subsequence("AGGTAB", "GXTXAYB"))  # Output: 4