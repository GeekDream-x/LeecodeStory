'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


# 1  400ms/18.2mb  93/17
class CQueue:

    def __init__(self):
        self.team = []
        self.front = 0
        self.rear = 0

    def appendTail(self, value: int) -> None:
        self.team.append(value)
        self.rear += 1


    def deleteHead(self) -> int:
        if self.team == []:
            return -1
        temp = self.team[0]
        self.team = self.team[1:]
        return temp


# 2 376/18.7 99/5  这才是真正用两个stack实现一个队列
class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    # 只有当out stack空了，才从in stack往里倒入数据
    def deleteHead(self) -> int:
        if not self.stack_out:
            if not self.stack_in:  # 都为空
                return -1
            else:  # 把in栈中的东西全部倒入out栈中
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()