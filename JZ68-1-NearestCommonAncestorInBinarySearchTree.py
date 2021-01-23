'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



 

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 分别获得到达两个结点的路径 然后从头找最后一个共同结点
# 76/18  96/10
# O(n)  O(n)
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         # 获得某个结点的路径
#         def findPath(root, target):
#             path = [root]
#             while root and root.val != target.val:
#                 if root.val > target.val:
#                     root = root.left
#                 else:
#                     root = root.right
#                 path.append(root)
#             return path

#         pPath = findPath(root, p)
#         qPath = findPath(root, q)

#         i = -1
#         while i <= len(pPath)-1 and i <= len(qPath)-1:

#             if i+1 > len(pPath)-1 or i+1 > len(qPath)-1 or pPath[i+1].val != qPath[i+1].val:
#                 return pPath[i]
#             else:
#                 i += 1

#         return 0

# 2 遍历root去找两个结点，如果root跟其中一个结点值相同或者两个结点前进方向不一致，直接返回root，同向则继续遍历
# 76/18  96/5
# O(n) O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            # 找到某个结点或两结点方向不一致
            if p.val == root.val or q.val == root.val or (p.val > root.val and q.val < root.val) or (
                    p.val < root.val and q.val > root.val):
                return root
            # 同向则继续
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                root = root.left

        return 0


# 3 官方 思路如方法2
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor


# 4 大佬递归  O(n)O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root



