'''
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 动态规划   60/93  O（n）O（n）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return None
        sum_list = [nums[0]]
        for i in range(1,len(nums)):
            sum_list.append(nums[i] if sum_list[i-1] <= 0 else nums[i] + sum_list[i-1])
        return max(sum_list)

# 2大佬简洁动态   O(n) O（1）64/18  87/44
# 因为有的时候，题目要求可能不能修改原有数组，考虑到在dp列表中，dp[i]只和dp[i-1]有关,所以用两个参数存储循环过程中的dp[i]和dp[i-1]的值即可
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:return None
        if len(nums) == 1: return nums[0]

        pre, cur, res = nums[0], 0, nums[0]
        for i in range(1,len(nums)):
            cur = nums[i] + max(pre, 0)
            pre = cur
            if res < pre: res = pre
        return res

