'''
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# 1 空间换时间 利用字典  36/15.5   97/23
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if not head:return None
#         # 复制原始链表，用next连接起来。同时<N, N’>放入字典。
#         res = head
#         node_dic = {}
#         previous_node = None
#         while head:
#             new_node = Node(head.val)
#             node_dic[head] = new_node
#             if previous_node:
#                 previous_node.next = new_node
#             previous_node = new_node
#             head = head.next

#         # 设置random
#         for node, new_node in node_dic.items():
#             new_node.random = node_dic[node.random] if node.random else None

#         return node_dic[res]


# 2  32/15.4   99/35  O(n)O(1)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            # pre.next = pre.next.next
            cur.next = cur.next.next
            # pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res  # 返回新链表头节点
