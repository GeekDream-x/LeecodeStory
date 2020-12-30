
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



# 2
# class CQueue:

#     def __init__(self):


#     def appendTail(self, value: int) -> None:


#     def deleteHead(self) -> int: