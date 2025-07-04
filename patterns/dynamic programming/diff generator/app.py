'''
Diff Utility
Given two similar strings, implement your own diff utility to list out all differences between them.
Diff Utility : It is a data comparison tool that calculates and displays the differences between two text.

Example
Input:
S1 = 'XMJYAUZ'
S2 = 'XMJAATZ'
Output:
XMJ-YA-U+A+TZ
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
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp

def diff_utility(s1,s2):
    dp=lcs(s1,s2)
    i=len(s1)
    j=len(s2)
    result=[]
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            result.append(s1[i-1])
            i-=1
            j-=1
        elif dp[i][j-1]>=dp[i-1][j]:
            result.append("+"+s2[j-1])
            j-=1
        else:
            result.append("-"+s1[i-1])
            i-=1
    while i>0:
        result.append('-'+s1[i-1])
        i-=1
    while j>0:
        result.append("+"+s2[j-1])
        j-=1
    return "".join(reversed(result))

# Example
s1 = "XMJYAUZ"
s2 = "XMJAATZ"
print(diff_utility(s1, s2)) # XMJ-YA-U+A+TZ

