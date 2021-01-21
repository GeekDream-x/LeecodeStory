'''
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

 

示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
 

限制：

1 <= n <= 10^5
1 <= m <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 创建n个数的列表 不断循环删除直到最后一个  2004/18 31/22
# class Solution:
#     def lastRemaining(self, n: int, m: int) -> int:

#         # 循环链表
#         loopList = [i for i in range(n)]

#         j = 0
#         loopListLen = len(loopList)
#         while loopListLen > 1:
#             j = (j+m-1) % loopListLen
#             loopList.pop(j)
#             loopListLen -= 1
#         return loopList[0]


# 2 公式推导+迭代  88/15  71/56

# class Solution:
#     def lastRemaining(self, n: int, m: int) -> int:
#         if n < 1 or m < 1 : return -1

#         i, last = 2,  0
#         while i <= n:
#             last = (last + m) % i
#             i += 1
#         return last



# 3 数学 + 递归  256/96
# Python 默认的递归深度不够，需要手动设置
#sys.setrecursionlimit(100000)

def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)