'''
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         null_flag = s=='' + p==''
#         if null_flag == 2:
#             return True
#         elif null_flag == 1:
#             return False

#         s_ptr = 0
#         p_ptr = 0
#         s_len = len(s)
#         p_len = len(p)

#         # 去掉星号后面与星号前面元素相同的元素
#         for i in range(p_len-1):
#             if p[i] == '*':
#                 if p[i+1] == p[i-1]:
#                     p = list(p)
#                     p.pop(i+1)
#                     p = ''.join(p)
#                     p_len -= 1


#         if p_len == 1:
#             if s_len > 1:
#                 return False
#             else:
#                 if s != p: return False
#                 return True

#         while s_ptr < s_len and p_ptr < p_len:

#             s_char = s[s_ptr]
#             if p_ptr+1 >= p_len:
#                 tmp = None
#             else:
#                 tmp = p[p_ptr + 1]
#             p_char = (p[p_ptr], tmp)

#             if p_char[1] != '*':
#                 # 后面不是*
#                 if p_char[0] == '.' or s_char == p_char[0]:
#                     s_ptr += 1
#                     p_ptr += 1
#                     continue
#                 else:
#                     return False

#             else:
#                 # 后面是* 则当前s串元素可以跟当前p串元素配对，也可跟星号后面元素的配对
#                 if p_char[0] == s_char or p_char[0] == '.':
#                     s_ptr += 1
#                 else:
#                     # 尝试与星号后面的元素配对
#                     if p_ptr + 2 >= p_len:
#                         # 星号是最后一位了
#                         return False
#                     else:
#                         if s_char != p[p_ptr + 2] and p[p_ptr + 2] != '.':
#                             return False
#                         else:
#                             #s_ptr += 1
#                             p_ptr += 2


#         dot_flag = 1
#         for x in p[p_ptr:]:
#             if x != '.':
#                 dot_flag = 0

#         omit_flag = 1
#         omit_char = p[p_ptr-1]
#         for i in range(p_ptr, p_len):
#             if i == p_len-1:
#                 combo = (p[i], None)
#                 if combo[0] == omit_char:
#                     break
#                 else:
#                     omit_flag = 0
#             else:
#                 combo = (p[i],p[i+1])

#             if combo[1] == '*':
#                 i += 1


#         if s_ptr == s_len and (p_ptr==p_len or (p_ptr == p_len-2 and p[-1] == '*') or dot_flag or omit_flag) :
#             # 匹配完成
#             return True
#         return False

# 2
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') \
                    if p[j - 1] == '*' else \
                    dp[i - 1][j - 1] and (p[j - 1] == '.' or s[i - 1] == p[j - 1])
        return dp[-1][-1]

