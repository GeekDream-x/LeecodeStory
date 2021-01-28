'''
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 自己后序遍历
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        def MirrorMidRootIterate(root):

            if not root: return None

            MirrorMidRootIterate(root.right)
            if self.count == k: return
            self.count += 1
            if self.count == k: self.res = root.val
            MirrorMidRootIterate(root.left)

        self.count = 0
        MirrorMidRootIterate(root)

        return self.res

# 2大佬递归
# 自己的看法解释一下为什么判断两次self.k : 可以试想一下当k == 1的时候不会返回，然后k减小1，然后遇到第二个self.k的判断，这个时候找到了正确的值。接着进入dfs(root.right),这个时候的self.k就已经是0了，就return返回，所以下面的递归就不会在执行了。
# class Solution:
#     def kthLargest(self, root: TreeNode, k: int) -> int:
#         def dfs(root):
#             if not root: return
#             dfs(root.right)
#             if self.k == 0: return
#             self.k -= 1
#             if self.k == 0: self.res = root.val
#             dfs(root.left)

#         self.k = k
#         dfs(root)
#         return self.res


# 3 迭代实现

# class Solution:
#     def kthLargest(self, root: TreeNode, k: int) -> int:
#         # 右根左 非递归遍历
#         stack,p,count = [],root,0
#         while p or stack:
#             while p:
#                 stack.append(p)
#                 p = p.right

#             curr = stack.pop()
#             count += 1
#             if count == k:return curr.val
#             p = curr.left