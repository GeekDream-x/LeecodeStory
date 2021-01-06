'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1 自己  失败
class Solution:
    real_root_val = None
    root_list = []
    first_call = True
    real_B = None
    found = False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B: return False
        if self.found: return True
        if self.first_call:
            self.real_root_val = B.val
            self.real_B = B
            self.first_call = False

        bool_left = bool_right = False

        if A.val == B.val:
            if A.val == self.real_root_val:
                self.root_list.append(True)

                # 判断以A B为根节点的两棵树是否相等
            if A.left and B.left:
                bool_left = self.isSubStructure(A.left, B.left)
            elif A.left == None and B.left == None:
                # 如果两棵树都没有左子树，什么也不用做，直接到柚子树的判断
                bool_left = True
            else:
                # 一个有一个没有
                bool_left = False
                if self.root_list != []:
                    self.root_list[-1] = False

            if A.right and B.right:
                bool_right = self.isSubStructure(A.right, B.right)
            elif A.right == None and B.right == None:
                # 如果两棵树都没有柚子树，什么也不用做，直接到柚子树的判断
                bool_right = True
            else:
                bool_right = False
                if self.root_list != []:
                    self.root_list[-1] = False

            # 当前结点是root时，判断左右子树是否都相等，相等才是True

            if self.root_list[-1] and A.val == self.real_root_val:
                self.found = True
                return True
                self.root_list = self.root_list[:-1]
                if bool_right and bool_left:
                    return True
                else:

                    return False
            else:
                # 当前结点不是root,却是False说明子树把他否定了
                if A.val == self.real_root_val: return False
                if bool_left or bool_right:
                    return True
                else:
                    return False

        else:
            # 两棵树根节点不相等，A 转向下一个结点，B不变，同时root设为False
            if self.root_list != []:
                self.root_list[-1] = False
            if A.left:
                bool_left = self.isSubStructure(A.left, self.real_B)
            if A.right:
                bool_right = self.isSubStructure(A.right, self.real_B)

            if bool_left or bool_right:
                return True
            else:
                return False


# 2 递归 先序遍历
'''
时间复杂度 O(MN)O(MN) ： 其中 M,NM,N 分别为树 AA 和 树 BB 的节点数量；先序遍历树 AA 占用 O(M)O(M) ，每次调用 recur(A, B) 判断占用 O(N)O(N) 。
空间复杂度 O(M)O(M) ： 当树 AA 和树 BB 都退化为链表时，递归调用深度最大。当 M \leq NM≤N 时，遍历树 AA 与递归判断的总递归深度为 MM ；当 M>NM>N 时，最差情况为遍历至树 AA 叶子节点，此时总递归深度为 MM。

'''


class Solution:
    # 先序遍历树 AA 中的每个节点 n_A
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 判断树 AA 中 以 n_A为根节点的子树 是否包含树 BB
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(4)
n11 = TreeNode(8)
n12 = TreeNode(9)

n1.left = n2
n1.right = n3
n3.left = n6
n3.right = n7
n2.left = n4
n2.right = n5
n4.left = n8
n4.right = n9

n10.left = n11
n10.right = n12

s = Solution()

print(s.isSubStructure(n1, n10))




