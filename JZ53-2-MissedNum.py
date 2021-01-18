'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 自己 二分查找 40/15  82/21
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         if nums == [0]: return 1
#         if nums == [1]: return 0
#         left, right = 0, len(nums)-1

#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == mid:
#                 # 缺失在右侧
#                 left = mid + 1
#             else:
#                 # 判断不是当前这个
#                 if mid == 0 or nums[mid - 1] == mid - 1:
#                     return mid
#                 # 在左侧
#                 right = mid - 1

#         # 缺失最后一个，也就是所有数字都在对应的位置上
#         if left == len(nums): return len(nums)


# 大佬二分
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i
