# 快排


def patition(nums, l, r):
    cur = l
    while l < r:
        print(l, r)
        while nums[cur] < nums[r]:
            r -= 1
            # 交换
        nums[cur], nums[r] = nums[r], nums[cur]
        cur = r

        while nums[cur] > nums[l]:
            l += 1
        nums[cur], nums[l] = nums[l], nums[cur]
        cur = l
    return l

def quickSort(nums):

    l, r = 0, len(nums ) -1
    patiIdx = patition(nums, l, r)
    quickSort(nums[0:patiIdx])
    quickSort(nums[patiIdx +1:])

quickSort([2 ,4 ,1 ,9 ,5])
