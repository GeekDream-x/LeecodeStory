

def editDistance(str1, str2):

    s1, s2 = list(str1), list(str2)
    len1, len2 = len(s1), len(s2)

    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # 初始化
    for i in range(len1):
        dp[i][0] = len2 + i
    for j in range(len2):
        dp[0][j] = len1 + j

    for i in range(1,len1+1):
        for j in range(1, len2+1):
            # 判断字符是否相同
            if s1[i-1] == s2[j-1]:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    return dp[-1][-1]


print(editDistance('xyowe', 'applewe'))