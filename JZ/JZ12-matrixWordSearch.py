'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
 

提示：

1 <= board.length <= 200
1 <= board[i].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import numpy as np



# 1 自己  384/33   6/5
# class Solution:
#     found = False
#     def exist(self, board: [[str]], word: str) -> bool:
#
#         # 1
#         row_num = len(board)
#         column_num = len(board[0])
#
#
#         def search(x, y, visited, word):
#             if self.found:
#                 return 1
#             if word == "":
#                 #print(visited)
#                 self.found = True
#                 return 1
#             candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
#             for can in candidates:
#                 can_x = can[0]
#                 can_y = can[1]
#                 if can_x < 0 or can_x >= row_num or can_y < 0 or can_y >= column_num or (can_x, can_y) in visited:
#                     # 越界了或被访问过
#                     continue
#                 elif board[can_x][can_y] == word[0]:
#                     # 匹配了当前首字符，继续遍历
#                     # print("!!!")
#                     # print(word[0])
#                     visited.append((can_x,can_y))
#                     search(can_x, can_y, visited, word[1:])
#
#             # 如果没匹配下一个字符，那么当前字符应当做没来过
#             visited.remove((x, y))
#
#         for i in range(row_num):
#             for j in range(column_num):
#                 visited = []
#
#                 # (i, j)搜索起始点
#                 if board[i][j] == word[0]:
#                     # 匹配第一个字母，成功匹配的开始
#
#                     print("!!")
#                     visited.append((i,j))
#                     # 搜索这个元素的上下左右元素，看是否匹配第二个字符
#                     search(i, j, visited, word[1:])
#                     if self.found == True:
#                         return True
#
#         return False


# 2 268/33 23/5   时间复杂度 O(3^K *MN)   空间复杂度 O(K)

# class Solution:
#
#     def exist(self, board: [[str]], word: str) -> bool:
#         def dfs(i, j, k):
#             if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
#             if k == len(word) - 1: return True
#             board[i][j] = ''
#             res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
#             board[i][j] = word[k]
#             return res
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(i, j, 0): return True
#         return False



# 3 非递归DFS 212/16   68/22
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        # 预处理
        w_l = len(word)
        if w_l < 1:
            return True
        rows = len(board)
        cols = len(board[0])
        # 标记数组
        board_vis = [[0] * cols for i in range(rows)]
        # 方向数组
        dir_list = [[-1, 0], [0, 1], [1, 0],[0, -1]]
        # 非递归DFS要用栈维护哦，先把所有头节点放进来，每个节点包括3个值（i,j,l）,i和j是它的坐标，l是它在word中的下标
        word_stack = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    word_stack.append((i, j, 0))
        # 正式开始DFS咯
        while len(word_stack) > 0:
            # 获取头节点信息，先不要弹出
            top = word_stack[-1]
            tx = top[0]
            ty = top[1]
            tl = top[2]
            # 访问这个节点，并开始深度遍历
            board_vis[tx][ty] = 1
            # 出口条件，如果word遍历完，返回True
            if tl == w_l - 1:
                return True
            # flag记录是否能够继续深度遍历
            flag = True
            for di in dir_list:
                next_x = tx + di[0]
                next_y = ty + di[1]
                # 深度遍历的条件
                if next_x >= 0 and next_x < rows and next_y >= 0 and next_y < cols \
                        and board_vis[next_x][next_y] == 0 and board[next_x][next_y] == word[tl + 1]:
                    # 注意子节点与父节点的关系
                    word_stack.append((next_x, next_y, tl + 1))
                    flag = False
            # 如果不能继续深度遍历，回溯，这个回溯有点复杂：需要一层一层往上回溯，回溯到有多个子节点的地方，类似于树的深度遍历
            if flag:
                while len(word_stack):
                    top = word_stack[-1]
                    if top[2] != tl:
                        break
                    tl -= 1
                    # 弹出，并标记取消
                    word_stack.pop()
                    board_vis[top[0]][top[1]] = 0
        return False



s = Solution()
print(s.exist(board=[["C","A","A"],["A","A","A"],["B","C","D"]], word="AAB"))




