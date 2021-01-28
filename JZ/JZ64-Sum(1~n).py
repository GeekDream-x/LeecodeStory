'''
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# 1 库函数   32/14.8  97/70
class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(n+1))


# 2 逻辑运算+递归   52/22  48/22
class Solution:
    res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res

# 3 逻辑运算+递归 简洁  44/25  71/5
class Solution:
    def sumNums(self, n: int) -> int:
        def Sum(m): return m and Sum(m-1)+m
        return Sum(n)


# 4 快速乘  32/15  97/66

class Solution:
    def sumNums(self, n: int) -> int:
        ans = 0
        A = n
        B = n + 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1
        ans += B & 1 and  A
        A <<= 1
        B >>= 1

        return ans>>1