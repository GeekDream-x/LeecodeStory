'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

 



 

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

 



 

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


# 1 自己 用list按中序遍历的顺序存起来然后改指针  40/16  88/9
# class Solution:
#     def treeToDoublyList(self, root: 'Node') -> 'Node':
#         if not root: return None
#         node_dic = []

#         # 中序遍历
#         def MidIterate(root):
#             # 遍历左子树,更新previous node
#             if root.left:MidIterate(root.left)
#             #遍历到root结点，添加到list
#             node_dic.append(root)
#             # 遍历右子树
#             if root.right:MidIterate(root.right)

#         MidIterate(root)
#         for i in range(len(node_dic)):
#             node_dic[i].left = node_dic[i-1]
#             node_dic[i].right = node_dic[i+1] if i < len(node_dic) - 1 else node_dic[0]
#         return node_dic[0]


# 2
# 时间复杂度 O(N)O(N) ： NN 为二叉树的节点数，中序遍历需要访问所有节点。
# 空间复杂度 O(N)O(N) ： 最差情况下，即树退化为链表时，递归深度达到 NN，系统使用 O(N)O(N) 栈空间。

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

