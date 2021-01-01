'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def minArray(self, numbers: [int]) -> int:
        # 1 40/15  66/18
        if numbers == []: return -1

        numbers_len = len(numbers)
        if numbers_len == 1 or numbers[0] < numbers[-1]: return numbers[0]

        for i in range(1, numbers_len):
            if numbers[i] < numbers[i - 1]:
                return numbers[i]

        return numbers[0]

        # 2 直接调库排序  36/15   86/15
        # numbers.sort()
        # return numbers[0]

        # 3 二分法 40/15   66/10

        # low, high = 0, len(numbers) - 1

        # while low < high:
        #     pivot = low + (high - low) // 2
        #     if numbers[pivot] > numbers[high]:
        #         low = pivot + 1
        #     elif numbers[pivot] < numbers[high]:
        #         high = pivot
        #     else:
        #         high -= 1
        # return numbers[high]








