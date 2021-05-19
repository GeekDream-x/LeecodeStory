# 快排


def patition(nums, l, r):
    target = nums[l]
    cur = l
    while l < r:
        print(l, r)
        while l < r and target <= nums[r]:
            r -= 1
            # 交换
        nums[cur], nums[r] = nums[r], nums[cur]
        cur = r

        while l < r and target >= nums[l]:
            l += 1
        nums[cur], nums[l] = nums[l], nums[cur]
        cur = l
    return l

def quickSort(nums):
    if len(nums) <= 1: return
    l, r = 0, len(nums)-1
    patiIdx = patition(nums, l, r)
    quickSort(nums[0:patiIdx])
    quickSort(nums[patiIdx +1:])
    print(nums)
#quickSort([2 ,4 ,1 ,9 ,5])






# ---------------------------------------------------------------
def quick_sort(alist, start, end):
    """快速排序"""

    if start >= end:
        return

    low, high = start, end
    pivot = alist[low]

    while low < high:
        while low < high and alist[high] >= pivot:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] <= pivot:
            low += 1
        alist[high] = alist[low]

    alist[low] = pivot

    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)




alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)