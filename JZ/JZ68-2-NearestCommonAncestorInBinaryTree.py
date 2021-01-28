'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 前序遍历 查找路径  84/28   45/5
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def findPath(root, target, path):

            path.append(root)

            if root.val == target.val:
                self.found = True
                return 1
            else:
                if root.left:
                    findPath(root.left, target, path)
                if not self.found and root.right:
                    findPath(root.right, target, path)

                    # 删掉当前root
            if self.found:
                return 1
            path.pop()

        pPath, qPath, self.found = [], [], False
        findPath(root, p, pPath)
        self.found = False
        findPath(root, q, qPath)

        # 寻找最后一个公共结点

        # 长路径截断
        pathLen = min(len(pPath), len(qPath))
        pPath, qPath, i = pPath[:pathLen], qPath[:pathLen], pathLen - 1

        # 从最后一个元素往前比较，遇到相同结点就返回
        while i >= 0:
            if pPath[i].val == qPath[i].val:
                return pPath[i]
            i -= 1
        return 0


# 2 大佬递归  60/26  99/23
# 时间复杂度 O(N) ： 其中 N 为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
# 空间复杂度 O(N) ： 最差情况下，递归深度达到 N ，系统使用 O(N) 大小的额外空间。

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root


# 3 大佬解析版
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 如果树为空，直接返回null
        if not root: return None
        # 如果 p和q中有等于 root的，那么它们的最近公共祖先即为root（一个节点也可以是它自己的祖先）
        if root == p or root == q: return root
        # 递归遍历左子树，只要在左子树中找到了p或q，则先找到谁就返回谁
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归遍历右子树，只要在右子树中找到了p或q，则先找到谁就返回谁
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果在左子树中 p和 q都找不到，则 p和 q一定都在右子树中，右子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        if not left:
            return right
        # 否则，如果 left不为空，在左子树中有找到节点（p或q），这时候要再判断一下右子树中的情况，如果在右子树中，p和q都找不到，则 p和q一定都在左子树中，左子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        elif not right:
            return left
        # 否则，当 left和 right均不为空时，说明 p、q节点分别在 root异侧, 最近公共祖先即为 root
        else:
            return root

