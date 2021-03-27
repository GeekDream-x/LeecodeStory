'''
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000


提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
'''


# 1 自己  双指针 60/15   34/43

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:

        i, j, count, totalNum = 0, 0, 0, len(nums1) + len(nums2)

        midCount = totalNum // 2 + 1 if totalNum % 2 != 0 else totalNum // 2

        tempList = []

        while i < len(nums1) or j < len(nums2):
            iTemp, jTemp = i, j
            if i < len(nums1) and j < len(nums2):
                # 两个数组都有数字
                if nums1[i] <= nums2[j]:
                    i += 1
                else:
                    j += 1
                count += 1
            elif i < len(nums1):
                # 只剩nums1
                count += 1
                i += 1
            else:
                # 只剩nums2
                count += 1
                j += 1

            # 判断是否添加数字到tempList
            if count >= midCount:
                if i != iTemp:
                    tempList.append(nums1[i - 1])
                else:
                    tempList.append(nums2[j - 1])

            # 判断是否数字找全
            if (len(tempList) == 1 and totalNum % 2 != 0) or (len(tempList) == 2 and totalNum % 2 == 0):
                return sum(tempList) / len(tempList)