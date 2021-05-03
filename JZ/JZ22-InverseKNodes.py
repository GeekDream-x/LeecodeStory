'''
剑指 Offer 22. 链表中倒数第k个节点
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1 自己 递归  36/15  86/5
class Solution:
    count = 0
    res_node = None
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        # 增强鲁棒性
        if head == None or k < 1: return None
        def getNext(node):
            if node.next != None:
                getNext(node.next)
            self.count += 1
            if k == self.count:
                self.res_node = node

        getNext(head)
        return self.res_node

# 2 双指针 指针A先走k-1步， 指针b出发。 A走到最后一个结点处，B指向的结点就是所求。  32/14.8
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


s = Solution()

print(s.getKthFromEnd(node1, 6))