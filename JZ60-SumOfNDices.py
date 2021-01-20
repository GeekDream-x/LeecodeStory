'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
 

限制：

1 <= n <= 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        times = [0 for _ in range(n * 6 + 1)]

        for i in range(1, n + 1):
            # 第i个骰子的1-6个面都要与n-1个骰子的所有加和相加  所有加和范围为[n-1:(n-1)*6]
            for j in range(1, 7):
                # 第i个骰子的数字为j
                for k in range(i - 1, (i - 1) * 6 + 1):
                    # print("K=",k)
                    times[j + k] += 1

            # 把当前骰子为0所产生的加和减掉1
            for m in range(i - 1, (i - 1) * 6 + 1):
                times[m] -= 1

        return [x / (6 ** n * 1.0) for x in times[n:]]