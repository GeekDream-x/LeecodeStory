'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 1
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        # 1 56/17  67/9
        def biggerThanK(x, y, k):
            return (x % 10 + y % 10 + (x // 10) % 10 + (y // 10) % 10 + x // 100 + y // 100) > k

        def dfs(i, j, k, vis):
            if not 0 <= i < m or not 0 <= j < n or biggerThanK(i, j, k) or vis[i][j] == 1: return 0

            vis[i][j] = 1
            nextChange = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for tup in nextChange:
                dfs(i + tup[0], j + tup[1], k, vis)

            return 1

        vis = [[0 for _ in range(n)] for _ in range(m)]

        dfs(0, 0, k, vis)
        return sum([sum(lis) for lis in vis])

s = Solution()

print(s.movingCount(1,2,1))