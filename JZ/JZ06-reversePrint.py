# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reversePrint(self, head: ListNode) -> list:
    # 1
    # lis = []
    # while head:
    #     lis.insert(0, head.val)
    #     head = head.next
    # return lis

    # 2 很慢 内存很大
    # if head is None:
    #     return []
    # return self.reversePrint(head.next) + [head.val]

    # 3
    lis = []
    while head:
        lis.append(head.val)
        head = head.next
    return lis[::-1]