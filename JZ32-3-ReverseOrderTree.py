'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 大佬
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: return []
#         res, deque = [], collections.deque([root])
#         while deque:
#             tmp = collections.deque()
#             for _ in range(len(deque)):
#                 node = deque.popleft()
#                 if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
#                 else: tmp.append(node.val) # 奇数层 -> 队列尾部
#                 if node.left: deque.append(node.left)
#                 if node.right: deque.append(node.right)
#             res.append(list(tmp))
#         return res


# 2模仿大佬
# from collections import deque
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:return []

#         res, stack = [], deque([root])

#         while stack:

#             tmp = deque([])

#             for _ in range(len(stack)):
#                 node = stack.popleft()
#                 if len(res) % 2:
#                     # 偶数层
#                     tmp.appendleft(node.val)
#                 else:
#                     tmp.append(node.val)
#                 if node.left:stack.append(node.left)
#                 if node.right:stack.append(node.right)

#             res.append(list(tmp))
#         return res


# 3 层序遍历+双端队列（奇偶逻辑分离，省了N次奇偶判断）
# 28/15  99/10

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:

#         if not root : return []

#         res, deque = [], collections.deque([root])

#         while deque:

#             tmp = []

#             for _ in range(len(deque)):
#                 node = deque.popleft()
#                 tmp.append(node.val)
#                 if node.left:deque.append(node.left)
#                 if node.right:deque.append(node.right)

#             res.append(tmp)

#             if not deque:break

#             tmp= []
#             for _ in range(len(deque)):
#                 node = deque.pop()
#                 tmp.append(node.val)
#                 izf node.right:deque.appendleft(node.right)
#                 if node.left:deque.appendleft(node.left)
#             res.append(tmp)
#         return res


# 4 层序遍历+倒序  32/15  97/24
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res



































