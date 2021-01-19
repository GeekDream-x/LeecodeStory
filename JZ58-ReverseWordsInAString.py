'''
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 自己正向遍历 存储单词 反向输出
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ""

        s = s.strip()
        res = []
        word = ""

        for i in range(len(s)):
            char = s[i]
            if char == ' ':

                if word != '':
                    # 说明到了word结束
                    res.append(word)
                    res.append(char)
                    word = ''
                else:
                    # 多余空格忽略
                    continue
            elif i == len(s) - 1:
                word += char
                res.append(word)
            else:
                # 当前是字母
                word += char
        return ''.join(res[::-1])


# 2 自己 反向遍历 截取单词 直接输出 41/15.3  51/9
class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()
        if s == "": return ""
        l, r, res = len(s) - 1, len(s) - 1, ""

        while l >= 0:

            while s[l] != ' ' and l >= 0:
                l -= 1

            # (l, r]为单词
            res += s[l + 1:r + 1] + ' '
            if l == -1: return res[:-1]
            while s[l] == ' ': l -= 1
            r = l


# 3 大佬一行  32/15.2  95/26
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
