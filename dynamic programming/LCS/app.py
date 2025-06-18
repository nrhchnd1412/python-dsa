'''
Given two sequences (usually strings) text1 and text2, find the length of their longest subsequence that appears in the same relative order, but not necessarily contiguous.

A subsequence is a sequence that appears in the same order but not necessarily contiguously.

Time/Space: O(m*n)
Space can be optmimized to O(n)
'''

def longest_common_subsequence(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

def space_optimized(s1,s2):
    # Time: O(m*n)
    # Space: O(n)
    m=len(s1)
    n=len(s2)
    prev=[0]*(n+1)
    current=[0]*(n+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                current[j]=1+prev[j-1]
            else:
                current[j]=max(prev[j],current[j-1])
        prev,current=current,[0]*(n+1)
    return prev[n]

def find_lcs_string(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    #backtrack to find lcs string
    result=[]
    while m>0 and n>0:
        if s1[m-1]==s2[n-1]:
            result.append(s1[m-1])
            m-=1
            n-=1
        elif dp[m][n-1]>=dp[m-1][n]:
            n-=1
        else:
            m-=1
    return ''.join(reversed(result))

print(longest_common_subsequence("abcde", "ace"))  # Output: 3
print(longest_common_subsequence("abc", "def"))    # Output: 0
print(longest_common_subsequence("AGGTAB", "GXTXAYB"))  # Output: 4
print(space_optimized("AGGTAB", "GXTXAYB"))  # Output: 4
print(find_lcs_string("XMJYAUZ","XMJAATZ")) # Output: XMJAZ