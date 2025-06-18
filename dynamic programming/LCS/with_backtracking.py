def all_LCS(s1, s2):
    m, n = len(s1), len(s2)

    # Step 1: Build the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    # Step 2: Backtrack to find all sequences
    from functools import lru_cache
    
    @lru_cache(None)
    def backtrack(i, j):
        if i == 0 or j == 0:
            return {""}
        elif s1[i-1] == s2[j-1]:
            return {seq + s1[i-1] for seq in backtrack(i-1, j-1)}
        else:
            results = set()
            if dp[i-1][j] >= dp[i][j-1]:
                results.update(backtrack(i-1, j))
            if dp[i][j-1] >= dp[i-1][j]:
                results.update(backtrack(i, j-1))
            return results

    lcs_set = backtrack(m, n)
    return sorted(seq[::-1] for seq in lcs_set)

# Example
S1 = "ABCBDAB"
S2 = "BDCABA"
result = all_LCS(S1, S2)
for seq in result:
    print(seq)
