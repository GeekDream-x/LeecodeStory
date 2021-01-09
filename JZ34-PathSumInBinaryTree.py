# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#1 自己递归  40/16  97/43
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:

        if not root: return []
        res, node_list = [], []
        def recur(root, sum_need, node_list):
            # 不管是不是叶子结点，都先加上这个结点，再去判断，跳出判断后recur函数最后统一删除
            node_list.append(root.val)
            if not root.left and not root.right:
                # 叶子结点 判断加和结果。路径总和刚好，则记录路径
                if root.val == sum_need:res.append(list(node_list))
            else:
                # 不是叶子结点
                sum_need -= root.val
                if root.left:recur(root.left, sum_need, node_list)
                if root.right:recur(root.right, sum_need, node_list)
            if node_list:node_list.pop()
        recur(root, sum, node_list)
        return res


n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(5)
n10 = TreeNode(1)

n11 = TreeNode(1)

n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.left = n9
n6.right = n10



s= Solution()

print(s.pathSum(n11, 1))



