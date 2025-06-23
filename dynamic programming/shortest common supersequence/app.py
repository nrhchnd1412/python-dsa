'''
The Shortest Common Supersequence (SCS) of two strings S1 and S2 is the shortest possible string that:

Contains both S1 and S2 as subsequences
(meaning you can delete some characters from the SCS to get both S1 and S2),
Preserves the order of characters in both S1 and S2,
And is as short as possible.

SCS(S1,S2)=len(S1)+len(S2)−LCS(S1,S2)

Time/Space: O(m*n)
'''

def lcs(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(
                    dp[i-1][j],
                    dp[i][j-1]
                )
    return dp[m][n]

def scs(s1,s2):
    lcs_len= lcs(s1,s2)
    return len(s1)+len(s2)-lcs_len

s1 = "ABCBDAB"
s2 = "BDCABA"

print(scs(s1,s2))
