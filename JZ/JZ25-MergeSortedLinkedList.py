'''
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

'''


class ListNode:
    def __init__(self, x):
            self.val = x
            self.next = None


# 1 自己  56/15  80/22
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        def merge(l1: ListNode, l2: ListNode):

            cur, aft = l1, l1.next
            while l2 and aft:
                if l2.val >= cur.val and l2.val <= aft.val:
                    l2next = l2.next

                    cur.next = l2
                    l2.next = aft
                    cur = l2

                    l2 = l2next

                elif l2.val > aft.val:
                    cur = cur.next
                    aft = aft.next

            if l2 is not None:
                # 全接在l1最后
                cur.next = l2
            return l1

        if not (l1 or l2):
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        if l1.val > l2.val:

            return merge(l2, l1)
        else:

            return merge(l1, l2)


# 2 伪头结点 48/15  97/20
# 时间复杂度 O(M+N) ： M,N 分别为链表 l_1，l_2的长度，合并操作需遍历两链表。
# 空间复杂度 O(1) ： 节点引用 dum , cur 使用常数大小的额外空间。
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/solution/mian-shi-ti-25-he-bing-liang-ge-pai-xu-de-lian-b-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return head.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)

n1.next = n2
n2.next = n3

n4.next = n5
n5.next = n6

s = Solution()

h = s.mergeTwoLists(n1,n4)

while h :
    print(h.val)
    h = h.next