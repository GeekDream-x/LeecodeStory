'''
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 1 520/18  11/21

import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_idx = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        # temp_stack = []
        # min_num = math.inf
        # while self.stack:
        #     cur_num = self.top()
        #     self.pop()
        #     if cur_num < min_num:
        #         min_num = cur_num

        #     temp_stack.append(cur_num)

        # self.stack = temp_stack[::-1]
        # return min_num
        return min(self.stack)


# 2 辅助栈 64/18  88/5
import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        cur_min = math.inf
        if self.min_stack != []:
            cur_min = self.min_stack[-1]
        self.min_stack.append(min(cur_min, x))

    def pop(self) -> None:
        self.min_stack = self.min_stack[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()