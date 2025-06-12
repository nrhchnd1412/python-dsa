'''
✅ Problem Statement
Given a string s, find the length of the longest subsequence of s that is a palindrome.

A subsequence is a sequence derived by deleting some or no elements without changing the order of the remaining elements.
Time/Space: O(n^2)
'''

def longest_palindrome_subsequence(s):
    n=len(s)
    dp=[[0]*n for _ in range(n)]

    # base case -- single char is a palindrome of length 1
    for i in range(n):
        dp[i][i]=1
    
    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
            if s[i]==s[j]:
                if length==2:
                    dp[i][j]=2
                else:
                    dp[i][j]=2+dp[i+1][j-1]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j-1])
    return dp[0][n - 1]
    

s = "bbbab"
print(longest_palindrome_subsequence(s))  # Output: 4 → "bbbb"