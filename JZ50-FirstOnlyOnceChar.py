'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 

限制：

0 <= s 的长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# 1 176/15  16/5  两个数组  O(n)O(n)
class Solution:
    def firstUniqChar(self, s: str) -> str:

        repeated = []
        once = []

        for i in range(len(s)-1, -1, -1):
            if s[i] in repeated:
                continue
            elif s[i] in once:
                once.remove(s[i])
                repeated.append(s[i])
            else:
                # 第一次出现
                once.append(s[i])



        return once[-1] if once else " "


# 2 哈希表 遍历s两次  80/15  89/5
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '


# 3 有序哈希表 遍历s一次 遍历dic一次  76/15  92/5
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '
