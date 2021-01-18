'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums.length <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 官方 functool 高阶函数模块 异或操作
# class Solution:
#     def singleNumbers(self, nums: List[int]) -> List[int]:
#         ret = functools.reduce(lambda x, y: x ^ y, nums)
#         div = 1
#         while div & ret == 0:
#             div <<= 1
#         a, b = 0, 0
#         for n in nums:
#             if n & div:
#                 a ^= n
#             else:
#                 b ^= n
#         return [a, b]


# 2 官方视频中没用高阶的解法
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        all_xor, a, b = 0, 0, 0

        # 求出所有数字异或的结果  也就是那两个只出现一次的数字异或的结果
        for num in nums:
            all_xor ^= num

        # 找到一位为1的位置
        pos = 1
        while not (pos & all_xor):
            pos <<= 1

        # 分组异或
        for num in nums:
            # !!!!这里判断一定要是为0 或者不写 反正不能 == 1。因为pos上为1的二进制数字，并不一定是1的二进制
            # 除非pos就是最后一位
            if num & pos == 0:
                a ^= num
            else:
                b ^= num

        return [a, b]