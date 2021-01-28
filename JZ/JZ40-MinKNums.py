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

# 时间复杂度：期望为 O(n)O(n) ，由于证明过程很繁琐，所以不再这里展开讲。具体证明可以参考《算法导论》第 9 章第 2 小节。

# 最坏情况下的时间复杂度为 O(n^2)。情况最差时，每次的划分点都是最大值或最小值，一共需要划分 n−1 次，而一次划分需要线性的时间复杂度，所以最坏情况下时间复杂度为 O(n^2)
# 空间复杂度：期望为 O(logn)，递归调用的期望深度为 O(logn)，每层需要的空间为O(1)，只有常数个变量。

# 最坏情况下的空间复杂度为 O(n)。最坏情况下需要划分 n 次，即 randomized_selected 函数递归调用最深 n−1 层，而每层由于需要 O(1) 的空间，所以一共需要O(n) 的空间复杂度。


# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         if not arr or not k:return []

#         def partition(arr, low, high):
#             target = arr[low]

#             while low < high:

#                 while low < high and arr[high] >= target:
#                     high -= 1
#                 arr[low], arr[high] = arr[high], arr[low]
#                 while low < high and arr[low] <= target:
#                     low += 1
#                 arr[low], arr[high] = arr[high], arr[low]

#             return low

#         start = 0
#         end = len(arr) - 1
#         index = partition(arr, start, end)
#         while index != k - 1:

#             if index > k - 1:
#                 end = index - 1
#                 index = partition(arr, start, end)
#             else:
#                 start = index + 1
#                 index = partition(arr,start, end)


#         return arr[:k]


# 4 大根堆  48/16  98/11
# 时间复杂度：O(n\log k)，其中 n 是数组 arr 的长度。由于大根堆实时维护前 k 小值，所以插入删除都是 O(logk) 的时间复杂度，最坏情况下数组里 n 个数都会插入，所以一共需要 O(n\log k) 的时间复杂度。

# 空间复杂度：O(k)O(k)，因为大根堆里最多 kk 个数。

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans







