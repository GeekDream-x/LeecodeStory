'''
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

 

提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 深度优先遍历 到达叶子结点就计算是否是最深 是的话更新
# 44/17  88/5
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def dfs(root):
            self.cur_depth += 1
            if not root.left and not root.right:
                # 到达叶子结点
                self.max_depth = max(self.max_depth, self.cur_depth)
            else:
                if root.left: dfs(root.left)
                if root.right: dfs(root.right)
            self.cur_depth -= 1

        if not root: return 0
        self.max_depth, self.cur_depth = 0, 0

        dfs(root)
        return self.max_depth


# 2 书上方法 40/16.7  96/5
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root: return 0
        left, right = 0, 0
        if root.left: left = self.maxDepth(root.left)
        if root.right: right = self.maxDepth(root.right)

        return left + 1 if left >= right else right + 1