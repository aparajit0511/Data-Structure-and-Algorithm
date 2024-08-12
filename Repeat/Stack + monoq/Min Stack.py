class MinStack:

    def __init__(self):
        self.stack = []
        self.Min_ = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.Min_) == 0:
            self.Min_.append(val)
        elif val <= self.Min_[-1]:
            self.Min_.append(val)

        
    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.Min_[-1]:
            self.Min_.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.Min_[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()