'''
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
 

提示：

-231 <= x <= 231 - 1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 将int转化为list 翻转求int
# 32/15  97/5   O(n) O(n)
class Solution:
    def reverse(self, x: int) -> int:

        if not x: return x

        num, negativeFlag = [], False

        if x < 0:
            negativeFlag = True
            x = -x

        while x:
            num.append(str(x % 10))
            x //= 10

        num = int("".join(num)) if not negativeFlag else -int("".join(num))

        return 0 if num > 2 ** 31 - 1 or num < - 2 ** 31 else num


# 2 好点的暴力法
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0


# 3 优化解法 O(logn) O(1)
class Solution:
    def reverse(self, x: int) -> int:

        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res