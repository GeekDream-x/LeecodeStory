'''
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3


'''



def findRepeatNumber(nums):
    # for i in range(len(nums)):
    #     if i == nums[i]:
    #         continue
    #     else:
    #         if nums[i] == nums[nums[i]]:
    #             return nums[i]
    #         else:
    #             while (nums[i] != i):
    #                 if nums[i] == nums[nums[i]]:
    #                     return nums[i]
    #
    #                 temp = nums[i]
    #                 nums[i] = nums[nums[i]]
    #                 nums[temp] = temp

    for i in range(len(nums)):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                index = nums[i]
                nums[i], nums[index] = nums[index], index



print(findRepeatNumber([2,4,5,6,1,3,5]))