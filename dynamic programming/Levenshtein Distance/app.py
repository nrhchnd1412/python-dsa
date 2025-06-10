'''
Given two strings str1 and str2, find the minimum number of operations required to convert str1 into str2. Allowed operations are:

Insert a character
Delete a character
Replace (Update) a character

Time complexity: O(n*m)
Space complexity O(m*n)
'''

def min_edit_distance(str1,str2):
    m=len(str1)
    n=len(str2)
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0]=i
    
    for j in range(n+1):
        dp[0][j]=j
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(
                    dp[i-1][j], #delete
                    dp[i][j-1], #insert
                    dp[i-1][j-1]
                )
    return dp[m][n]


print(min_edit_distance("horse", "ros"))  # Output: 3