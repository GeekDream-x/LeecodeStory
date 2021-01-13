'''
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
 

限制：

0 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1找规律  36/14.8  78/11
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10: return n

        i, n = 2, n + 1 - 10
        while 1:

            # 当前位数的数总共的个数
            cur_totalNum = 9 * (10 ** (i - 1)) * i

            if n > cur_totalNum:
                # 当前位数的数字所占长度满足不了n
                n -= cur_totalNum
                i += 1
            else:
                # n就在当前i位数的范围内

                # 变成索引来操作
                n -= 1
                # 定位第几个i位数
                idx_1 = n // i

                # 这个数是
                targetNum = 10 ** (i - 1) + idx_1

                # 定位第idx+1个i位数的第几位
                idx_2 = n % i

                # 精确定位

                targetNum //= 10 ** (i - idx_2 - 1)

                return targetNum % 10


# 2 大佬 32/14.8 93/6
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:  # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit  # 2.
        return int(str(num)[(n - 1) % digit])  # 3.
