'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 自己 144/16   5/5
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         def print_mat(matrix, index, lis):

#             # 定位起点
#             start_x = index
#             start_y = index


#             # 越过中线可以停止了
#             if start_x >= len(matrix) // 2 + 0.5 or start_y >= len(matrix[0]) // 2 + 0.5: return None


#             # 上边
#             while start_x == index and start_y <= (len(matrix[0])-index-1):
#                 #if start_y >= 1:print(lis)
#                 lis.append(matrix[start_x][start_y])

#                 if start_y == (len(matrix[0])-index-1):
#                     start_x += 1
#                     break
#                 start_y += 1

#             # 右边
#             while start_y == (len(matrix[0])-index-1) and start_x <= (len(matrix)-index-1):
#                 lis.append(matrix[start_x][start_y])


#                 if start_x == (len(matrix)-index-1):
#                     start_y -= 1
#                     break
#                 start_x += 1
#             # 下边
#             while start_x == (len(matrix)-index-1) and start_y >= index and start_y <= (len(matrix[0])-index-1):
#                 lis.append(matrix[start_x][start_y])

#                 if start_y == index:
#                     start_x -= 1
#                     break
#                 start_y -= 1

#             # 左边
#             while start_y == index and start_x >= index + 1 and start_x <= (len(matrix)-index-1):
#                 lis.append(matrix[start_x][start_y])


#                 if start_x == index + 1 :
#                     break
#                 start_x -= 1


#         lis = []
#         if matrix == []:return []

#         min_len = min(len(matrix), len(matrix[0]))
#         iteration_num = min_len // 2 if min_len % 2 == 0 else min_len // 2 + 1
#         for i in range(iteration_num):
#             print_mat(matrix, i, lis)
#             print(lis)
#         return lis


# 2 大佬解法 64/15  21/24
# class Solution:
#     def spiralOrder(self, matrix:[[int]]) -> [int]:
#         if not matrix: return []
#         l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
#         while True:
#             for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
#             t += 1
#             if t > b: break
#             for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
#             r -= 1
#             if l > r: break
#             for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
#             b -= 1
#             if t > b: break
#             for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
#             l += 1
#             if l > r: break
#         return res


# 大佬2 60/15   28/10
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res