'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# import numpy

# 1 递归实现动态规划 矩阵存储中间结果
# 借助numpy ：192/31  5/5
# 不用numpy：60/17 40/5
# class Solution:
#     def maxValue(self, grid: List[List[int]]) -> int:

#         def dp(i,j):
#             if wealth[i][j]:
#                 return wealth[i][j]
#             if i == 0 and j == 0:
#                 wealth[i][j] = grid[i][j]

#             elif i == 0: wealth[i][j] = dp(i,j-1) + grid[i][j]
#             elif j == 0: wealth[i][j] = dp(i-1,j)+ grid[i][j]
#             else:
#                 wealth[i][j] = max(dp(i-1,j), dp(i,j-1)) + grid[i][j]
#             return wealth[i][j]


#         # wealth = numpy.zeros(numpy.array(grid).shape)
#         wealth = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]


#         return int(dp(len(grid)-1,len(grid[0])-1))


# 2 循环实现动态规划 矩阵存储中间结果
# 新建二维数组存储 44/16  97/7
# 直接修改原数组  36/16  99/21
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:

        # m, n = len(grid), len(grid[0])
        # wealth = [[0 for _ in range(n)] for _ in range(m)]
        # wealth[0][0] = grid[0][0]
        # # 直接填充第一列和第一行
        # for i in range(1,m):
        #     wealth[i][0] = grid[i][0] + wealth[i-1][0]
        # for j in range(1,n):
        #     wealth[0][j] = grid[0][j] + wealth[0][j-1]

        # # 从（1，1）开始按行填充
        # for i in range(1, m):
        #     for j in range(1, n):
        #         wealth[i][j] = max(wealth[i-1][j], wealth[i][j-1]) + grid[i][j]

        # return wealth[-1][-1]

        m, n = len(grid), len(grid[0])

        # 直接填充第一列和第一行
        for i in range(1, m):
            grid[i][0] = grid[i][0] + grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] = grid[0][j] + grid[0][j - 1]

            # 从（1，1）开始按行填充
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]


# 3 只用长度为n的数组记录中间结果
# 48/15  91/60

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        wealth = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                left, up = 0, 0
                if i > 0: up = wealth[j]
                if j > 0: left = wealth[j - 1]
                wealth[j] = max(up, left) + grid[i][j]
        return wealth[-1]















