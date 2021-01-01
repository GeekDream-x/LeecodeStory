import numpy as np


class Solution:
    def exist(self, board: [[str]], word: str) -> bool:

        # 1
        row_num = len(board)
        column_num = len(board[0])
        word_len = len(word)

        def search(x, y, visited, word):
            if word == []: return True
            candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for can in candidates:
                x = can[0]
                y = can[1]
                if x < 0 or x >= row_num or y < 0 or y >= column_num or visited[i][j] == 1:
                    # 越界了或被访问过
                    continue
                elif board[x][y] == word[0]:
                    # 匹配了当前首字符，继续遍历
                    search(x, y, visited, word[1:])

        for i in range(row_num):
            for j in range(column_num):
                visited = np.zeros((row_num, column_num))

                # (i, j)搜索起始点
                if board[i][j] == word[0]:
                    # 匹配第一个字母，成功匹配的开始
                    visited[i][j] = 1
                    # 搜索这个元素的上下左右元素，看是否匹配第二个字符
                    search(i, j, visited, word[1:])

        return False



s = Solution()
print(s.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED"))




