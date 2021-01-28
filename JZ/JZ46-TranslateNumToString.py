'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 1 自己 动态 用数组存储结果  44/15
# class Solution:
#     def translateNum(self, num: int) -> int:
#         if num < 10: return 1

#         combo_nums = [1]
#         num_list = [int(char) for char in str(num)]

#         # 处理idx = 1的数的翻译种类数

#         combo_nums.append(2 if num_list[0] == 1 or (num_list[0] == 2 and num_list[1] <= 5) else 1)


#         for i in range(2,len(num_list)):
#             combo_nums.append(combo_nums[-1] + combo_nums[-2] \
#             if num_list[i-1] == 1 or (num_list[i-1] == 2 and num_list[i] <= 5) else combo_nums[-1])

#         return combo_nums[-1]


# 2 自己 动态 升级 用两个变量存储结果  32/14  93/25   O（n） O（n）
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10: return 1

        num_list = [int(char) for char in str(num)]

        # 处理idx = 1的数的翻译种类数
        pre, cur = 1, 2 if (num_list[0] * 10 + num_list[1]) < 26 else 1

        for i in range(2, len(num_list)):
            pre, cur = cur, pre + cur if (num_list[i - 1] * 10 + num_list[i]) < 26 and num_list[i - 1] != 0 else cur

        return cur


# 3 大佬 空间复杂度为O(1)，因为没创建数字列表。从右到左依次遍历
class Solution:
    def translateNum(self, num: int) -> int:
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
            y = x
        return a

