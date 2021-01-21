'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 自己 先排序再遍历 O(n) 28/15   99/10
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        zeroNum, preNumIndex, missNum, i = 0, -1, 0, 0
        nums.sort()

        while i < len(nums):
            if nums[i] == 0:
                zeroNum += 1
            else:
                if preNumIndex != -1:
                    # 如果有相同的数，直接False
                    if nums[i] == nums[preNumIndex]: return False
                    # 之前有非0的数，记录中间缺失几个数
                    missNum += nums[i] - nums[preNumIndex] - 1

                preNumIndex = i

            i += 1
        return True if missNum <= zeroNum else False



