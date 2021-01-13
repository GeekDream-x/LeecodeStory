'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
 

限制：

最多会对 addNum、findMedian 进行 50000 次调用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# 1 调库函数  1156/25  18/9
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.team = []

#     def addNum(self, num: int) -> None:
#         self.team.append(num)

#     def findMedian(self) -> float:
#         self.team.sort()
#         team_len = len(self.team)
#         if team_len % 2 == 0:
#             # 偶数个元素
#             return (self.team[team_len // 2 - 1] + self.team[team_len // 2]) / 2
#         else:
#             return self.team[team_len // 2]


# 2 最大堆最小堆  188/25  96/5
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.min_heap = []
#         self.max_heap = []

#     def addNum(self, num: int) -> None:

#         #mid_small = -self.max_heap[0]
#         mid_large = self.min_heap[0] if self.min_heap else -math.inf

#         len_min_heap = len(self.min_heap) if self.min_heap else 0
#         len_max_heap = len(self.max_heap) if self.max_heap else 0

#         if num >= mid_large:
#             # 待插入数字比最小堆顶点大，应该放入最小堆

#             # 判断两堆结点数，看是否可以直接插入
#             if len_min_heap <= len_max_heap:
#                #最小堆结点不多，则直接插入最小堆
#                heapq.heappush(self.min_heap, num)
#             else:
#                 # 最小堆堆结点多，把最小堆堆顶挤到最大堆，再将当前数字插入最小堆
#                 heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
#                 heapq.heappush(self.min_heap, num)
#         else:
#             # 待插入数字比最小堆顶点小，应该放入最大堆
#             if len_min_heap >= len_max_heap:
#                 # 最大堆结点不多，直接插入最大堆
#                 heapq.heappush(self.max_heap, -num)
#             else:
#                 # 最大堆结点多

#                 if num >= -self.max_heap[0]:
#                     # 若当前数字大于等于最大堆顶点，则应插入最小堆
#                     heapq.heappush(self.min_heap, num)
#                 else:
#                     # 当前数字小于最大堆顶点，应插入最大堆，同时最大堆顶点进入最小堆
#                     heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
#                     heapq.heappush(self.max_heap, -num)


#     def findMedian(self) -> float:

#         len_min_heap = len(self.min_heap)
#         len_max_heap = len(self.max_heap)

#         if len_min_heap == len_max_heap:
#             return (self.min_heap[0] + (-self.max_heap[0])) / 2
#         else:
#             return self.min_heap[0] if len_min_heap > len_max_heap else -self.max_heap[0]


# 3 大佬两个堆  168/25  100/9
# from heapq import *

# class MedianFinder:
#     def __init__(self):
#         self.A = [] # 小顶堆，保存较大的一半
#         self.B = [] # 大顶堆，保存较小的一半

#     def addNum(self, num: int) -> None:
#         if len(self.A) != len(self.B):
#             heappush(self.B, -heappushpop(self.A, num))
#         else:
#             heappush(self.A, -heappushpop(self.B, -num))

#     def findMedian(self) -> float:
#         return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0