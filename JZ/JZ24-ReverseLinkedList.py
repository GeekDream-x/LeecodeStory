'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1   32/15.5   98/18
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        befNode = None
        while head:
            tmp = head.next
            head.next = befNode
            befNode = head
            if tmp != None:
                head = tmp
            else:
                return head
        return None


# 2 递归  36/20
# 时间复杂度 O(N)O(N) ： 遍历链表使用线性大小时间。
# 空间复杂度 O(N)O(N) ： 遍历链表的递归深度达到 NN ，系统使用 O(N)O(N) 大小额外空间。


class Solution:
    resNode = None

    def reverseList(self, head: ListNode) -> ListNode:

        if head == None: return None

        def recur(currentNode):
            if currentNode.next != None:
                # 没到达链表最后一个结点
                befNode = recur(currentNode.next)
                befNode.next = currentNode
            else:
                self.resNode = currentNode
            return currentNode

        tailNode = recur(head)
        tailNode.next = None
        return self.resNode


# 3 大佬递归   32/20
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre  # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回
