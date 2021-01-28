class Solution:

    # 1 动态规划 36/14.8
    # def numWays(self, n: int) -> int:

    #     if n == 0 or n == 1:
    #         return 1

    #     ways = [1,1]

    #     for i in range(2, n+1):
    #         ways.append(ways[i-1] + ways[i-2])

    #     return ways[n] % 1000000007



    # 2 动态规划优化存储  28/14.7    98/16
    def numWays(self, n: int) -> int:

        if n == 0 or n == 1:
            return 1

        a, b = 1, 1

        for i in range(2, n + 1):
            a, b = b, a + b

        return b % 1000000007
