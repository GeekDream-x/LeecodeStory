'''
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 时间限制  在非丑数上浪费了大量时间计算
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        def isUglyNum(num):
            while num % 5 == 0:
                if num in uglyNums: return True
                num //= 5

            while num % 3 == 0:
                if num in uglyNums: return True
                num //= 3

            while num % 2 == 0:
                if num in uglyNums: return True
                num //= 2

            if num == 1:
                return True
            return False

        uglyNums = [1, 2, 3, 4, 5]
        if n < 6: return uglyNums[n - 1]

        count, ptr = 5, 5
        while count < n:
            ptr += 1

            if isUglyNum(ptr):
                uglyNums.append(ptr)
                count += 1
        return uglyNums[-1]


# 2 O(N) O（N）
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1 for _ in range(n)], 0, 0, 0

        for i in range(1, n):
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            # 因为如果abc得出的值有相同的，那么都要向前走一步
            if dp[i] == dp[a] * 2: a += 1
            if dp[i] == dp[b] * 3: b += 1
            if dp[i] == dp[c] * 5: c += 1

        return dp[-1]