'''
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8


'''


# 1 自己回溯 208/21  31/15
# class Solution:
#     def permutation(self, s: str) -> List[str]:

#         def permute(s):
#             if len(s) == 1:
#                 # 排列结束
#                 tmp.append(s[0])
#                 string = "".join(tmp)
#                 if string not in res.keys(): res[string]=True
#                 tmp.pop()
#                 return 1
#             for i in range(0, len(s)):
#                 scopy = s.copy()
#                 if scopy[0] != scopy[i] or i == 0:
#                     scopy[0], scopy[i] = scopy[i], scopy[0]
#                     tmp.append(scopy[0])
#                     permute(scopy[1:])
#                     tmp.pop()

#         s = list(s)
#         res, tmp = {}, []
#         permute(s)

#         return list(res.keys())

# 2 根据大佬的做法，去掉for循环每次复制字符串s, 但是影响不大
# class Solution:
#     def permutation(self, s: str) -> List[str]:

#         def permute(s):
#             if len(s) == 1:
#                 # 排列结束
#                 tmp.append(s[0])
#                 string = "".join(tmp)
#                 if string not in res.keys(): res[string]=True
#                 tmp.pop()
#                 return 1
#             for i in range(0, len(s)):
#                 if s[0] != s[i] or i == 0:
#                     s[0], s[i] = s[i], s[0]
#                     tmp.append(s[0])
#                     permute(s[1:])
#                     tmp.pop()
#                     s[0], s[i] = s[i], s[0]

#         s = list(s)
#         res, tmp = {}, []
#         permute(s)

#         return list(res.keys())


# 3 大佬 112/19   83/34

class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue  # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res
