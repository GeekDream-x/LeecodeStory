# 一、输入: x是n*d的矩阵, w是d*m的矩阵，b是d*1的向量，keep_prob为保持隐藏神经元比例。
# 输出: y=wx+b，但随机隐藏比例为keep_prob的神经元。
#
#
# 可以导入的库: random

import random
def dropout(x, w, b, p):

    def listMul(l1, l2, drop):
        res = 0
        for i in range(len(l1)):

            res += l1[i]*l2[i] if i not in drop else 0
        return res

    def getCol(B, x):
        res = []
        for line in B:
            res.append(line[x])
        return res

    def matMulti(A, B, b, p):

        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

        # 获得当前需要drop的神经元的序号
        drop = []
        for d in range(len(B)):
            randNum = random.random()
            if randNum > p:
                drop.append(d)

        for i in range(len(res)):

            rowA = A[i]

            for j in range(len(res[0])):

                colB = getCol(B, j)


                res[i][j] = listMul(rowA, colB, drop) + b[j]

        return res


    return matMulti(x, w, b, p)

print(dropout([[2, 1, 3], [4, 4, 2]],[[3, 1], [3, 2], [2, 5]],[1,3], 0.5))