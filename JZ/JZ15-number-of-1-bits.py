

class Solution:
    def hammingWeight(self, n: int) -> int:


        # 1 36/14.8  85/5
        '''
        时间复杂度 O(log_2 n)： 此算法循环内部仅有 移位、与、加 等基本运算，占用 O(1)O(1) ；逐位判断需循环 log_2 n次，其中 log_2 代表数字 n 最高位 1 的所在位数（例如 log_2 4 = 2, log_2 16 = 4。
        空间复杂度 O(1)O(1) ： 变量 resres 使用常数大小额外空间。

        '''
        # count = 0
        #
        # while n > 0:
        #     isone = n % 10
        #     if isone: count += 1
        #     n = n // 10
        #
        # return count

        # 2 40/14.7  67/13
        # return bin(n).count('1')

        # 3 巧用n-1  36/14/6  85/18
        '''
        (n−1) 解析： 二进制数字 n 最右边的 1 变成 0，此 1 右边的 0 都变成 1 。
        n&(n−1) 解析： 二进制数字 n 最右边的 1 变成 0 ，其余不变。

        时间复杂度 O(M)： n&(n−1) 操作仅有减法和与运算，占用 O(1) ；设 M为二进制数字 n 中 1的个数，则需循环 M 次（每轮消去一个 1 ），占用 O(M) 。
        空间复杂度 O(1)： 变量 count使用常数大小额外空间。


        '''
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count


s = Solution()

