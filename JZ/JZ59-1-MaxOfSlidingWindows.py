'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 库函数得到窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        i, numsLen, res = 0, len(nums), []

        while i <= numsLen - k:
            res.append(max(nums[i:i + k]))

            i += 1

        return res


# 2 window+库函数  52/18  99/32   O(nk)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        if k == 1: return nums
        i, j, windowMax, maxI, res = 0, 0, nums[0], len(nums) - k, []

        # 处理第一个window
        while j - i + 1 < k:
            j += 1
            if nums[j] > windowMax:
                windowMax = nums[j]
        if j != 0: res.append(windowMax)

        # window滑行
        while i < maxI:
            if nums[i] == windowMax:
                windowMax = max(nums[i + 1:j + 1])
            i += 1
            j += 1
            if nums[j] > windowMax:
                windowMax = nums[j]
            res.append(windowMax)

        return res


# 3 ***单调双端队列  56/18  97/5
# 时间复杂度 O(n) ： 其中n为数组nums长度；线性遍历nums 占用O(N)；每个元素最多仅入队和出队一次，因此单调队列deque占用O(2N)
# 空间复杂度 O(k) ： 双端队列deque中最多同时存储k个元素（即窗口大小）。


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        if k == 1: return nums

        i, j, maxTeam, res = 0, 0, collections.deque([nums[0]]), []

        # 窗口扩大到k
        # [i,j]元素个数 <= k - 1
        while j - i + 1 <= k - 1:
            j += 1
            curNum = nums[j]
            while maxTeam and curNum > maxTeam[-1]:
                maxTeam.pop()
            maxTeam.append(curNum)
        res.append(maxTeam[0])

        # 窗口滑动
        while j < len(nums) - 1:
            # 左边界前进
            if nums[i] == maxTeam[0]:
                maxTeam.popleft()
            i += 1

            # 右边界前进
            j += 1
            curNum = nums[j]
            while maxTeam and curNum > maxTeam[-1]:
                maxTeam.pop()
            maxTeam.append(curNum)

            res.append(maxTeam[0])

        return res

































