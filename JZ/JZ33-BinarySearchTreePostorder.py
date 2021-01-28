'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# 1
# 平台报错：RecursionError: maximum recursion depth exceeded while calling a Python object
# 本地没问题
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        if len(postorder) <= 1: return True

        i = 0
        root = postorder[-1]

        while i < len(postorder):
            if postorder[i] > root:
                i -= 1
                break
            i += 1
        for j in range(i, len(postorder) - 1):
            if postorder[j] < root:
                return False
        return self.verifyPostorder(postorder[0:i + 1]) and self.verifyPostorder(postorder[i + 1:-1])



# 2 递归分治
# 时间复杂度 O(N^2)每次调用 recur(i,j) 减去一个根节点，因此递归占用O(N) ；最差情况下（即当树退化为链表），每轮递归都需遍历树所有节点，占用 O(N)。空间复杂度 O(N)： 最差情况下（即当树退化为链表），递归深度将达到 N 。


# class Solution:
#     def verifyPostorder(self, postorder: List[int]) -> bool:

#         def recur(start, end):
#             # 任意两个数都可以构成搜索树的后序遍历。
#             if start >= end - 1:return True
#             root = postorder[end]
#             i = start
#             while i < end:
#                 if postorder[i] > root:break
#                 i += 1
#             for j in range(i, end):
#                 if postorder[j] < root: return False
#             # 左子树为空会导致i=start, 导致递归时下一轮recur左子树时start > end
#             return recur(start, i-1) and recur(i,end-1)
#         return recur(0, len(postorder)-1)




# 3 大佬递归分治 32/15  95/11
# class Solution:
#     def verifyPostorder(self, postorder: [int]) -> bool:
#         def recur(i, j):
#             if i >= j: return True
#             p = i
#             while postorder[p] < postorder[j]: p += 1
#             m = p
#             while postorder[p] > postorder[j]: p += 1
#             return p == j and recur(i, m - 1) and recur(m, j - 1)

#         return recur(0, len(postorder) - 1)



# 4









s = Solution()
print(s.verifyPostorder([1,6,3,2,5]))