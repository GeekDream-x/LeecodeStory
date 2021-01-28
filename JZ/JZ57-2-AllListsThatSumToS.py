'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 自己 window  136/14.8  59/33
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:

        left, right, window, windowSum, res = 1, 2, [1, 2], 3, []
        rightMax = (target // 2) + 1
        while right <= rightMax:

            if windowSum < target:
                # window的和小了，right前进，window添加新元素
                right += 1
                windowSum += right
                window.append(right)
                continue
            elif windowSum > target:
                # window的和太大了, 若只有两个元素，直接返回，后面越来越大，如果有多的元素，去掉左端元素
                if len(window) == 2: break
            else:
                # 找到合适window，加入res
                res.append(window)

            windowSum -= left
            left += 1
            window = window[1:]

        return res


# 2 不用window记录 因为下标就代表数字， 所以直接range即可 108ms
# def findContinuousSequence(self, target: int) -> List[List[int]]:
#     i = 1 # 滑动窗口的左边界
#     j = 1 # 滑动窗口的右边界
#     sum = 0 # 滑动窗口中数字的和
#     res = []

#     while i <= target // 2:
#         if sum < target:
#             # 右边界向右移动
#             sum += j
#             j += 1
#         elif sum > target:
#             # 左边界向右移动
#             sum -= i
#             i += 1
#         else:
#             # 记录结果
#             arr = list(range(i, j))
#             res.append(arr)
#             # 左边界向右移动
#             sum -= i
#             i += 1

#     return res

# 3 自己等差数列  152/15  53/10
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        head, tail, res, tailMax = 1, 2, [], target // 2 + 1

        while tail <= tailMax:
            idx = tail - head + 1
            curSum = idx * head + idx * (idx - 1) // 2

            if curSum < target:
                tail += 1
                continue
            if curSum == target:
                res.append([x for x in range(head, tail + 1)])
            head += 1

        return res

    # 4 牛逼！ 大佬逆用等差数列求和公式，求a1


# 32/15  99/8

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for n in range(2, target + 1):
            tmp = target * 2 - n * (n - 1)
            if tmp <= 0: break
            if tmp % (2 * n) == 0:
                # 能找到一个整数a1
                a1 = tmp // (2 * n)
                res.append([a1 + i for i in range(n)])
        return res[::-1]


