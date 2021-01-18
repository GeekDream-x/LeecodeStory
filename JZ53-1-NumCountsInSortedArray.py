'''
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

限制：

0 <= 数组长度 <= 50000



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 O（n） 低效  遍历一遍数组
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        count = 0
        for num in nums:
            if num == target: count += 1
        return count


# 2 官方思路 二分法 迭代查找  28/15.7  99/5
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if len(nums) == 0:return 0
#         # flag: 0为找第一个  1为找第二个
#         def getMIndex(l, r, flag):
#             if l > r:return -1
#             mid = l + (r-l) // 2
#             if nums[mid] > target:
#                 return getMIndex(l, mid-1, flag)
#             elif nums[mid] < target:
#                 return getMIndex(mid+1, r, flag)
#             else:
#                 # mid = target 判断是不是最边上的
#                 if (flag == 0 and ( mid == 0 or nums[mid-1] != target)) or \
#                 (flag == 1 and (mid == len(nums)-1 or nums[mid+1] != target)):
#                     # 找到第一个 # 找到最后一个
#                     return mid
#                 else:
#                     # 找到中间的target
#                     return getMIndex(l, mid-1, flag) if flag == 0 else getMIndex(mid+1, r, flag)
#         first = getMIndex(0, len(nums)-1, 0)
#         end = getMIndex(0, len(nums)-1, 1)

#         return end - first + 1 if first != -1 and end != -1 else 0


# 3 大佬 循环二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i, j = 0, len(nums) - 1

        # 寻找右边界（最后一个target的下一个元素的位置）
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] <= target:
                # 相等的时候，说明右边界肯定在[mid+1, j]里，所以更新i进行右侧搜索
                i = mid + 1
            else:
                j = mid - 1

        if j >= 0 and nums[j] != target: return 0
        right = i
        # i, j = 0, right   # 不可，因为若为空数组，此时i=j=0, 下面的while循环就能进去，就会报错out of range
        i = 0

        # 寻找左边界
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                # 相等的时候，说明左边界肯定在[i,mid-1]里，所以更新j进行左侧搜索
                j = mid - 1

        left = j

        return right - left - 1



































