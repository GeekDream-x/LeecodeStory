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


# 2 书上方法 快排思想查找边界
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return 0

        # flag: 0为找第一个  1为找第二个
        def getMIndex(l, r, flag):
            if l > r: return -1
            mid = l + (r - l) // 2
            if nums[mid] > target:
                return getMIndex(l, mid - 1, flag)
            elif nums[mid] < target:
                return getMIndex(mid + 1, r, flag)
            else:
                # mid = target 判断是不是最边上的
                if (flag == 0 and (mid == 0 or nums[mid - 1] != target)) or \
                        (flag == 1 and (mid == len(nums) - 1 or nums[mid + 1] != target)):
                    # 找到第一个 # 找到最后一个
                    return mid

                else:
                    # 找到中间的target
                    if flag == 0:
                        return getMIndex(l, mid - 1, flag)
                    else:
                        return getMIndex(mid + 1, r, flag)

        first = getMIndex(0, len(nums) - 1, 0)
        end = getMIndex(0, len(nums) - 1, 1)

        return end - first + 1 if first != -1 and end != -1 else 0