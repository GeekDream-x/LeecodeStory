'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# 1 直接用库  36/16  99/22
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         # 1
#         # counter = collections.Counter(nums)
#         # nums_len = len(nums) / 2
#         # for item in counter.items():
#         #     if item[1] > nums_len: return item[0]

#         # 2 40/16
#         return collections.Counter(nums).most_common(1)[0][0]





# 2 先排序再循环统计  44/16  88/21
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         curCount = 0
#         curNum = nums[0]
#         for num in nums:
#             if num == curNum:curCount += 1
#             else:
#                 curCount, curNum = 1, num
#                 continue
#             if curCount > len(nums) / 2:
#                 return curNum

# 3 排序后直接返回中位数   36/16  99/5
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]



# 4 摩尔投票法  O(n)O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x
