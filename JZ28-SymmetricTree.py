'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1 递归
# class Solution:
#     def sym(self, root: TreeNode, root2:TreeNode):
#         if not(root or root2):return True
#         if not root or not root2 or root2.val != root.val:return False
#         return self.sym(root.left, root2.right) and self.sym(root.right, root2.left)

#     def isSymmetric(self, root: TreeNode) -> bool:
#         return self.sym(root.left,root.right) if root else True


# 2 迭代
# class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is None:
    #         return True
    #     q = []
    #     q.append(root.left)
    #     q.append(root.right)
    #     while len(q) != 0:
    #         A = q.pop(0)
    #         B = q.pop(0)
    #         if A == None and B == None:
    #             continue
    #         if A == None or B == None:
    #             return False
    #         if A.val != B.val:
    #             return False
    #         q.append(A.left)
    #         q.append(B.right)
    #         q.append(A.right)
    #         q.append(B.left)
    #     return True

    # 3 模仿2 我


from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        q = deque([root.left, root.right])

        while len(q):
            node1 = q.popleft()
            node2 = q.popleft()

            if not node1 and not node2: continue
            if not node1 or not node2 or node1.val != node2.val: return False

            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)

        return True

