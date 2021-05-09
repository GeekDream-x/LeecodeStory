# n, m, k = input().strip().split()
#
# cost = [[-1 for _ in range(int(m))] for _ in range(int(n))]
#
# cost [0][0] = 0
#
# for _ in range(int(k)):
#
#     line = input().strip().split()
#
#     startx = int(line[0]) - 1
#     starty = int(line[1]) - 1
#     endx = int(line[2]) - 1
#     endy = int(line[3]) - 1
#     costCur = int(line[4])
#
#     if cost[startx][starty] == -1:
#         continue
#
#     newCost = costCur + cost[startx][starty]
#     cost[endx][endy] = newCost if cost[endx][endy] == -1 else min(cost[endx][endy], newCost)
#
#
# print(cost[-1][-1])


n, m, h = input().strip().split()

n, m, h = int(n), int(m), int(h)

heights = input().strip().split()

heights = [int(x) for x in heights]

count = 0
start = -1
for i in range(n):

    if heights[i] <= h:
        if count == 0:
            start = i
        count += 1
        if count == m:
            print(start + 1)
            break
    else:
        # 当前木桩过不去
        start = -1
        count = 0

if count != m:
    print(-1)