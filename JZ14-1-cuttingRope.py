'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 动态规划 40/14.7 70/14
# class Solution:
#     def cuttingRope(self, n: int) -> int:


#         if n < 2: return 0
#         if n == 2: return 1
#         if n == 3: return 2

#         maxProducts = [0, 0, 1, 2]

#         for i in range(4, n + 1):
#             max_i = 0
#             for j in range(1, i // 2 + 1):

#                 #max_ij = max(j * maxProducts[i - j], j * (i - j))
#                 max_ij = max(j, maxProducts[j]) * max(i-j, maxProducts[i-j])

#                 if max_ij > max_i:
#                     max_i = max_ij

#             maxProducts.append(max_i)

#         return maxProducts[-1]


# 2 动态规划简洁版  36/14   87/10   时间复杂度：O(N^2) 空间复杂度：O(N)。
# class Solution:
#     def cuttingRope(self, n: int) -> int:
#         dp = [0 for _ in range(n+1)]
#         dp[2] = 1 # 初始化base case
#         for i in range(3, n+1):
#             for j in range(1, i//2+1):
#                 dp[i] = max(dp[i], j * (i - j), j * dp[i-j])
#         return dp[n]


# 3动态规划升级版

# 我们发现任何大于 3的数都可以拆分为数字 1，2，3的和，且它们对 33 的余数总是 0，1，2，因此我们可以仅用 dp[0]，dp[1]，dp[2] 表示所有大于 3 的值，这样空间复杂度可降到 O(1)。

# class Solution:
#     def cuttingRope(self, n: int) -> int:
#         dp = [0, 1, 1]
#         for i in range(3, n + 1):
#             dp[i % 3] = max(
#                 1 * max(i - 1, dp[(i - 1) % 3]),
#                 2 * max(i - 2, dp[(i - 2) % 3]),
#                 3 * max(i - 3, dp[(i - 3) % 3])
#             )
#         return dp[n % 3]


# 4 32/14  95/14  找规律，尽可能分出更多的3     时间复杂度：O(1)。空间复杂度：O(1)。
# 理论推导：https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4: return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return pow(3, a)
        elif b == 1:
            return pow(3, a - 1) * 4
        else:
            return pow(3, a) * 2







s = Solution()

print(s.cuttingRope(10))

