'''
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

 

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
 

说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

'''



# 1 失败

# class Solution:
#     def myPow(self, x: float, n: int) -> float:

#         ans = 1
#         if fabs(x) - 0 <= 1e-5: return 0
#         if n == 0 or fabs(fabs(x) - 1) < 1e-6: return 1
#         if n == 0: return 1

#         if n > 0:
#             for _ in range(n):
#                 ans *= x
#             return ans
#         else:
#             for _ in range(n, 0):
#                 ans *= x
#             return 1 / ans


# 2 快速幂  32/14.8  95/10
# 时间复杂度 O(log_2 n)： 二分的时间复杂度为对数级别。
# 空间复杂度 O(1) ： res, b 等变量占用常数大小额外空间。
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/di-gui-xie-fa-fen-zhi-si-xiang-yu-fei-di-gui-xie-f/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 1: return x
        if n < 0:
            x = 1 / x
            # 负数变成正数
            n = -n

        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        return res