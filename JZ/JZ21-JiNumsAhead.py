'''
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。



示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000

'''




# 1 双指针 56/18.8  67/16  O(n)/O(1)
class Solution:
    def exchange(self, nums: [int]) -> [int]:

        head, tail = 0, len(nums) - 1
        while head < tail:
            if nums[head] % 2 == 0:
                if nums[tail] % 2 != 0:
                    # 头偶尾奇，交换
                    temp = nums[head]
                    nums[head] = nums[tail]
                    nums[tail] = temp
                    head += 1
                else:
                    tail -= 1
            else:
                head += 1
        return nums


s = Solution()

print(s.exchange([2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]))