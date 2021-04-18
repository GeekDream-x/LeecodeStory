'''
给你一个字符串 s （下标从 0 开始）。你需要对 s 执行以下操作直到它变为一个有序字符串：

找到 最大下标 i ，使得 1 <= i < s.length 且 s[i] < s[i - 1] 。
找到 最大下标 j ，使得 i <= j < s.length 且对于所有在闭区间 [i, j] 之间的 k 都有 s[k] < s[i - 1] 。
交换下标为 i - 1​​​​ 和 j​​​​ 处的两个字符。
将下标 i 开始的字符串后缀反转。
请你返回将字符串变成有序的最少操作次数。由于答案可能会很大，请返回它对 109 + 7 取余 的结果。

 

示例 1：

输入：s = "cba"
输出：5
解释：模拟过程如下所示：
操作 1：i=2，j=2。交换 s[1] 和 s[2] 得到 s="cab" ，然后反转下标从 2 开始的后缀字符串，得到 s="cab" 。
操作 2：i=1，j=2。交换 s[0] 和 s[2] 得到 s="bac" ，然后反转下标从 1 开始的后缀字符串，得到 s="bca" 。
操作 3：i=2，j=2。交换 s[1] 和 s[2] 得到 s="bac" ，然后反转下标从 2 开始的后缀字符串，得到 s="bac" 。
操作 4：i=1，j=1。交换 s[0] 和 s[1] 得到 s="abc" ，然后反转下标从 1 开始的后缀字符串，得到 s="acb" 。
操作 5：i=2，j=2。交换 s[1] 和 s[2] 得到 s="abc" ，然后反转下标从 2 开始的后缀字符串，得到 s="abc" 。
示例 2：

输入：s = "aabaa"
输出：2
解释：模拟过程如下所示：
操作 1：i=3，j=4。交换 s[2] 和 s[4] 得到 s="aaaab" ，然后反转下标从 3 开始的后缀字符串，得到 s="aaaba" 。
操作 2：i=4，j=4。交换 s[3] 和 s[4] 得到 s="aaaab" ，然后反转下标从 4 开始的后缀字符串，得到 s="aaaab" 。
示例 3：

输入：s = "cdbea"
输出：63
示例 4：

输入：s = "leetcodeleetcodeleetcode"
输出：982157772
 

提示：

1 <= s.length <= 3000
s​ 只包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-operations-to-make-string-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 自己 "leetcode"超时
class Solution:
    def makeStringSorted(self, s: str) -> int:
        s = list(s)
        count, i, j = 0, 0, 0
        foundI = False
        limit = pow(10, 9) + 7

        while True:
            # 无序才继续

            # 寻找i
            for i in range(len(s) - 1, 0, -1):
                if s[i] < s[i - 1]:
                    foundI = True
                    break

            if not foundI:
                # 字符串有序了，找不到i了
                return count

            # 寻找j
            for j in range(i, len(s)):
                if s[j] > s[i - 1]:
                    j -= 1
                    break

            # 交换j 和 i-1
            s[j], s[i - 1] = s[i - 1], s[j]

            head = s[:i]
            tail = s[i:]
            tail.reverse()
            s = head + tail
            count += 1

            if count == limit:
                count = 0

            foundI = False