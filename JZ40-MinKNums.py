'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 56/15.7  88/30
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         arr.sort()
#         return arr[0:k]


# 2  996/15.7  5/27  因为max()调用很多次和删除元素遍历res消耗时间，导致总运行时间很长
# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         if not arr or not k:return []
#         res = arr[:k]
#         curMax = max(res)

#         for i in range(k, len(arr)):
#             if arr[i] < curMax:
#                 res.remove(curMax)
#                 res.append(arr[i])
#                 curMax = max(res)

#         return res


# 3 可修改数组时，利用partition函数  快排思想 112/15.8  30/22
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or not k: return []

        def partition(arr, low, high):
            target = arr[low]

            while low < high:

                while low < high and arr[high] >= target:
                    high -= 1
                arr[low], arr[high] = arr[high], arr[low]
                while low < high and arr[low] <= target:
                    low += 1
                arr[low], arr[high] = arr[high], arr[low]

            return low

        start = 0
        end = len(arr) - 1
        index = partition(arr, start, end)
        while index != k - 1:

            if index > k - 1:
                end = index - 1
                index = partition(arr, start, end)
            else:
                start = index + 1
                index = partition(arr, start, end)

        return arr[:k]



