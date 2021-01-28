'''
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

限制：

1 <= 树的结点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 发现不平衡就返回 不再遍历  40/19 100/5
# 时间复杂度 O(N)： N 为树的节点数；最差情况下，需要递归遍历树的所有节点。
# 空间复杂度 O(N)： 最差情况下（树退化为链表时），系统递归需要使用 O(N)的栈空间。

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def balanceSearch(root):
            if not root: return 0

            left_depth = balanceSearch(root.left)
            right_depth = balanceSearch(root.right)
            if abs(left_depth - right_depth) > 1: self.unbalance = True

            # 如果已经发现不平衡 直接返回1直到退出递归
            return 1 if self.unbalance else max(left_depth, right_depth) + 1

        self.unbalance = False
        balanceSearch(root)
        return not self.unbalance