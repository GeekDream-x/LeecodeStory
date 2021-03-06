# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
只适用于无重复数字

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        # 1


        # if preorder == []:
        #     return None
        # root = TreeNode(preorder[0])
        # root_idx_inorder = inorder.index(root.val)
        # root.left = self.buildTree(preorder=preorder[1:root_idx_inorder + 1], inorder=inorder[0:root_idx_inorder])
        # root.right = self.buildTree(preorder=preorder[root_idx_inorder + 1:], inorder=inorder[root_idx_inorder + 1:])
        # return root


        # 2  更快更小
        # if inorder:
        #     ind = inorder.index(preorder.pop(0))
        #     root = TreeNode(inorder[ind])
        #     root.left = self.buildTree(preorder, inorder[0:ind])
        #     root.right = self.buildTree(preorder, inorder[ind + 1:])
        #     return root

        # 3 44ms/19mb
        def recur(root, left, right):
            if left > right: return  # 递归终止
            node = TreeNode(preorder[root])  # 建立根节点
            i = dic[preorder[root]]  # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)  # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right)  # 开启右子树递归
            return node  # 回溯返回根节点

        dic, preorder = {}, preorder
        # 遍历中序遍历列表，构建字典存结点和对应的索引
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)



sol = Solution()

print(sol.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]).right.left.left)