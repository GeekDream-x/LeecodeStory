'''
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 自己 根据大佬的优化 广度优先序列化 借助队列   124/19.2 80/9
'''
时间复杂度 O(N)： N为二叉树的节点数，层序遍历需要访问所有节点，最差情况下需要访问 N+1 个null，总体复杂度为 O(2N + 1) = O(N) 。
空间复杂度 O(N)： 最差情况下，队列 queue 同时存储 \frac{N+1}{2}个节点（或N+1个 null ），使用 O(N) ；列表 res 使用O(N) 。
'''


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "[]"
        res, node_list = [], collections.deque([root])
        while node_list:
            node = node_list.popleft()
            if node:
                res.append(str(node.val))
                node_list.append(node.left)
                node_list.append(node.right)
            else:
                res.append('null')

        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return None
        vals = data[1:-1].split(',')
        i = 1
        head = TreeNode(int(vals[0]))
        queue = collections.deque([head])
        while queue:
            cur_node = queue.popleft()
            if not vals:
                break

            if vals[i] != 'null':
                new_node1 = TreeNode(int(vals[i]))
                cur_node.left = new_node1
                queue.append(new_node1)
            i += 1

            if vals[i] != 'null':
                new_node2 = TreeNode(int(vals[i]))
                cur_node.right = new_node2
                queue.append(new_node2)
            i += 1
        return head

# 2 大佬原版 120/19.5  88/16
# class Codec:
#     def serialize(self, root):
#         if not root: return "[]"
#         queue = collections.deque()
#         queue.append(root)
#         res = []
#         while queue:
#             node = queue.popleft()
#             if node:
#                 res.append(str(node.val))
#                 queue.append(node.left)
#                 queue.append(node.right)
#             else: res.append("null")
#         print(','.join(res))
#         return '[' + ','.join(res) + ']'

#     def deserialize(self, data):
#         if data == "[]": return
#         vals, i = data[1:-1].split(','), 1
#         root = TreeNode(int(vals[0]))
#         queue = collections.deque()
#         queue.append(root)
#         while queue:
#             node = queue.popleft()
#             if vals[i] != "null":
#                 node.left = TreeNode(int(vals[i]))
#                 queue.append(node.left)
#             i += 1
#             if vals[i] != "null":
#                 node.right = TreeNode(int(vals[i]))
#                 queue.append(node.right)
#             i += 1
#         return root

