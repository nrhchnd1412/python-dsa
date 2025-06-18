'''
Given a string s, find the length of the longest subsequence which appears at least twice in the string, 
without overlapping at the same indices.

📌 Subsequence: A sequence that can be derived by deleting some or no elements without changing the order.
📌 Repeated: The subsequence must appear at least twice, but at different indices.
'''

def longest_repeated_subsequence(s):
    # Time: O(n^2)
    # Space: O(n^2)
    n = len(s)
    dp=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1]==s[j-1] and i!=j:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n][n]

def space_optimized(s):
    # Time: O(n^2)
    # Space: O(n)
    n=len(s)
    prev=[0]* (n+1)
    curr=[0]*(n+1)
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (n + 1)
    return prev[n]

print(longest_repeated_subsequence("aab"))
print(longest_repeated_subsequence("aabebcdd"))
print(longest_repeated_subsequence("xyzxyz"))
print(space_optimized("xyzxyz"))