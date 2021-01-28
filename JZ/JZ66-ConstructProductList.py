'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 

提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 书上 动态规划构建乘积数组  64/24   90/6
# O(n)  O(n)
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:

        cList, dList = [1 for _ in range(len(a))], [1 for _ in range(len(a))]

        for i in range(1, len(a)):
            cList[i] = cList[i - 1] * a[i - 1]
        for j in range(len(a) - 2, -1, -1):
            dList[j] = dList[j + 1] * a[j + 1]

        for k in range(len(a)):
            cList[k] *= dList[k]
        return cList


# 2  O(n)  O(1)  用tmp一个变量来记录每一步的上三角
# 64/22  91/43

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1] * len(a), 1

        # 构造下三角
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]

        # 乘上上三角
        for j in range(len(a) - 2, -1, -1):
            tmp *= a[j + 1]
            b[j] *= tmp
        return b
