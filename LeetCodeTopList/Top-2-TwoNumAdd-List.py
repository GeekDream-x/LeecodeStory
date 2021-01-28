'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 自己 将两个链表数组化，从前往后相加进位，遍历的同时生成新的结点，加入到结果链表中
# O(n) O(n)   48/15   100/23
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # if not l1.val: return l2
        # if not l2.val: return l1

        l1List, l2List = [], []
        while l1:
            l1List.append(l1.val)
            l1 = l1.next
        while l2:
            l2List.append(l2.val)
            l2 = l2.next

        lenDiff = len(l1List) - len(l2List)
        if lenDiff > 0:
            # l1长, 补全l2
            l2List = l2List + [0] * lenDiff
        elif lenDiff < 0:
            l1List = l1List + [0] * (-lenDiff)

        # 现在两个list一样长，从前往后相加
        preNode, carryFlag, i, res, cur, pre = None, False, 0, None, None, None

        while i <= len(l1List) - 1:

            carry = 1 if carryFlag else 0
            curSum = l1List[i] + l2List[i] + carry
            carryFlag = False

            if curSum < 10:
                cur = ListNode(curSum)
            else:
                cur = ListNode(curSum % 10)
                carryFlag = True

            # 连接结点
            if pre:
                # 前面已经创建过结点，则设置next
                pre.next = cur

            pre = cur

            if i == 0:
                res = cur

            if i == len(l1List) - 1 and carryFlag:
                # 加到了最后一位，如果还有进位，那么需要新建结点赋值为1
                cur = ListNode(val=1)
                pre.next = cur
                return res

            i += 1

        return res


# 2 大佬遍历   60/15  98/5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        dummy = p = ListNode(None)
        s = 0  # 初始化进位 s 为 0
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)  # p.next 指向新链表, 用来创建一个新的链表
            p = p.next  # p 向后遍历
            s //= 10  # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None  # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None  # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next  # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点
