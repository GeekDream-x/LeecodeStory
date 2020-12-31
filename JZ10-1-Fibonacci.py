'''
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
 

提示：

0 <= n <= 100

'''


# # 1 不记录小问题结果 每次都要重新计算
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0: return 0
#         if n == 1: return 1
#         return (self.fib(n - 1) + self.fib(n - 2)) % 1000000007


# 2 32/14.7   93/14  记录了子问题结果，再遇到直接从dic中查询即可
class Solution:
    dic = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = (self.fib(n - 1) + self.fib(n - 2)) % 1000000007
        return self.dic[n]