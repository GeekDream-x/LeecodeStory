'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

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
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        lis = []
        count = 0
        layer = 0
        nodes = [root] if root else []
        nodes_layer = []
        while nodes:
            node = nodes.pop(0)
            count += 1
            if node:
                nodes_layer.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)

            if (count + 1) == 2 ** (layer + 1):
                lis.append(nodes_layer)
                nodes_layer = []
                layer += 1

        return lis

n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
# n4 = TreeNode(None)
# n5 = TreeNode(None)
n6 = TreeNode(15)
n7 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n6
n3.right = n7


s = Solution()

print(s.levelOrder(n1))