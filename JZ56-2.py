'''
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

 

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
 

限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 自己根据书上思路
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        bits = [0 for _ in range(31)]

        for num in nums:
            i = 0
            while i < 31:
                bits[i] += num & 1
                num >>= 1

                if num == 0:
                    break

                i += 1

        for idx, val in enumerate(bits):
            bits[idx] = 0 if val % 3 == 0 else 1

        bits = bits[::-1]
        res = 0
        print(bits)
        for bit in bits:
            res |= bit
            res <<= 1

        return res >> 1


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         res = 0
#         for i in range(32):
#             cnt = 0  # 记录当前 bit 有多少个1
#             bit = 1 << i  # 记录当前要操作的 bit
#             for num in nums:
#                 if num & bit != 0:
#                     cnt += 1
#             if cnt % 3 != 0:
#                 # 不等于0说明唯一出现的数字在这个 bit 上是1
#                 res |= bit

#         return res - 2 ** 32 if res > 2 ** 31 - 1 else res


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

# 有限状态自动机
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ones, twos = 0, 0
#         for num in nums:
#             ones = ones ^ num & ~twos
#             twos = twos ^ num & ~ones
#         return ones

