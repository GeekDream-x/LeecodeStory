import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        # write code here
        if not head: return None
        pre, cur = ListNode(math.inf), head
        res = pre
        cf = None
        while cur.next:
            cf = cur.val
            while cur.next and cf == cur.next.val:
                cur = cur.next
            if not cur.next:break
            cur = cur.next
            if not cur.next or cur.val != cur.next.val:
                pre.next = cur
                pre = cur
        pre.next = cur
        print(res.next.val)
        return res.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)

n1.next = n2
n2.next = n3

s = Solution()
s.deleteDuplicates(n1)