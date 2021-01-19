'''
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 傻瓜操作 超时
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for num in nums:
#             if target - num in nums and (target-num) != num:
#                 return [num, target-num]

#         return[]


# 1 自己 二分查找 884/25  5/40   O(NlogN)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for idx, num in enumerate(nums):
            # 如果当前数大于target则break
            if num >= target: break

            # 如果补数<=当前数，后面一定不存在，则跳过
            pair = target - num
            if pair <= num: continue

            # 后面可能存在补数
            i, j = idx + 1, len(nums) - 1
            while i <= j:
                mid = i + (j - i) // 2
                if nums[mid] > pair:
                    # 当前区间的中位数比补数大，则补数在左侧
                    j = mid - 1
                elif nums[mid] < pair:
                    # 当前区间的中位数比补数小，则补数在右侧
                    i = mid + 1
                else:
                    # 当前位置就是补数
                    return [num, pair]
        return []


# 2 window双指针法  104/25   99/47
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        left, right = 0, len(nums) - 1

        while left < right:
            addSum = nums[left] + nums[right]
            if addSum > target:
                # 减小大数
                right -= 1
            elif addSum < target:
                # 增大小数
                left += 1
            else:
                # 找到了
                return [nums[left], nums[right]]

        return []




























