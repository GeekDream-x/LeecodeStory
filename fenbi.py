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
quickSort([2 ,4 ,1 ,9 ,5])






# ---------------------------------------------------------------
def quick_sort(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)