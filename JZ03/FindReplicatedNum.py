
def findRepeatNumber(nums):
    for i in range(len(nums)):
        if i == nums[i]:
            continue
        else:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                while (nums[i] != i):
                    if nums[i] == nums[nums[i]]:
                        return nums[i]

                    temp = nums[i]
                    nums[i] = nums[nums[i]]
                    nums[temp] = temp



print(findRepeatNumber([2,4,5,6,1,3,5]))