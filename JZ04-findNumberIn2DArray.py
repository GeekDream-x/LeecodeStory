'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# import numpy as np


def findNumberIn2DArray(self, matrix: [[int]], target: int) -> bool:
    # 1
    # return (target in np.array(matrix))

    # 2
    # if matrix == [] or matrix == [[]]:
    #     return False
    #
    # n, m = len(matrix), len(matrix[0])
    # for i in range(n):
    #     min_num, max_num = matrix[i][0], matrix[i][-1]
    #
    #     if target >= min_num and target <= max_num:
    #         # 可能在这个list
    #         for j in range(m):
    #             if matrix[i][j] == target:
    #                 return True
    #
    # return False

    # 3 官方解法  time:O(n+m)  space(1)
    if matrix == [] or matrix == [[]]:
        return False

    i, j, rows = 0, len(matrix[0]) - 1, len(matrix)
    corner = matrix[i][j]

    while target != corner:

        if target > corner:
            i += 1
        else:
            j -= 1

        if i == rows or j < 0:
            return False

        corner = matrix[i][j]

    return True


    # 4 简洁 这是从左下角出发
    i, j = len(matrix) - 1, 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > target: i -= 1
        elif matrix[i][j] < target: j += 1
        else: return True
    return False

'''
从左下出发快还是从右上出发快，取决于具体的matrix和target.同样的数据，两者运行时间可能相差10ms
'''