# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        # 1
        if not preorder:
            return None
        loc = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1: loc + 1], inorder[: loc])
        root.right = self.buildTree(preorder[loc + 1:], inorder[loc + 1:])
        return root

