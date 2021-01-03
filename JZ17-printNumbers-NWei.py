'''
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 1 52/20  37/19   时间复杂度 O(10^n) 生成长度为 10^n的列表需使用 O(10^n) 时间。
# 空间复杂度 O(1)： 建立列表需使用 O(1)大小的额外空间（ 列表作为返回结果，不计入额外空间 ）。

# class Solution:
#     def printNumbers(self, n: int) -> List[int]:

#         max_num = 9
#         for i in range(n-1):
#             max_num *= 10
#             max_num += 9

#         res = []
#         for i in range(1,max_num+1):
#             res.append(i)

#         return res


