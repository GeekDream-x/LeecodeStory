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


# 2 28/20  99/20   与方法一思路一样，但是缩为一个循环，更节省时间
# class Solution:
#     def printNumbers(self, n: int) -> List[int]:
#         res = []
#         for i in range(1, 10 ** n):
#             res.append(i)
#         return res



# 3
# class Solution:
#     def printNumbers(self, n: int) -> [int]:
#         return list(range(1, 10 ** n))




# 4 112/20  9/6    解决大数问题
class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res

# 5 对4注释解读
class Solution:
    # easy solution witout thinking about large number
    '''
    def myPow(self, x: float, n: int) -> float:
        if x==0:  return 0        # 1. 避免 幂为负数 的时候的，将其变换到分母出错
        if n<0:                    #  2. 幂为负数时，将其准换为正数，因此，底数 x 需要变成 1 / x
            x = 1 / x
            n = -n
        res=1
        while n:                    # 3. 当幂等于0的时候，则跳出循环，因为任何数的 0 次幂 等于1，res乘1 等于其本身
            if n & 1: res *= x     # 4. 奇数
            x *= x                   # 5. 平方项
            n >>= 1                 # 6. 将至 n // 2
        return res

    def printNumbers(self, n: int) -> List[int]:
         return [i for i in range(1,self.myPow(10,n))]
    '''

    def printNumbers(self, n: int) -> [int]:
        def dfs(x):  # x 代表的是 第x层： 0 <= x < n

            if x == n:  # 最多是 n-1 层（从0开始计数），如果到达了第 n 层，则代表可以返回
                s = ''.join(num[self.start:])  # 将一维nums 数组中的元素，从左边界start开始拼接成字符串 s
                if s != '0': res.append(int(s))  # 如果 s == “ 0 ”, 则忽略；否则将其append 到结果数组res中
                if n - self.start == self.nine: self.start -= 1  # 当前满足边界向前的公式，n- start== nine(nine: s中9的数量)，则左边界左移一步。
                return  # 只有在n层返回到第n-1层时才会用到，其他的从 n-1 返回到 n-2层 不是通过这个路径，而是执行完最后一行，默认return

            for i in range(10):
                if i == 9: self.nine += 1  # 如果当前遍历到9，则 9 会增加到字符串中，于是nine 加 1
                num[x] = str(i)  # 当前层的值 固定为 str(i)
                dfs(x + 1)  # 进入下一层进行全排列遍历
            # 从 n-1 返回到 n-2层，n-2层到 n-3层时，才会进行nine-1 的操作；因为从 n层返回到 n-1层并没有增加数字的操作，只有拼接
            self.nine -= 1

        num, res = ["0"] * n, []  # 创建大小为 n 层的 中间变量数组 num; 空结果数组res
        # 初始化
        self.nine = 0
        self.start = n - 1  # 由于是从 0 开始，递增遍历，于是左边界初始化为最右 ,即 n-1
        dfs(0)  # 从 1 开始
        return res

