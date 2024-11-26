class MinStack:
    # keeping track of most recent min along the current value
    # def __init__(self):
    #     self.stack = []
        
    # def push(self, val: int) -> None:
    #     curr_min = self.getMin()
    #     self.stack.append((val, min(curr_min, val)))
        
    # def pop(self) -> None:
    #     self.stack.pop()

    # def top(self) -> int:
    #     if not self.stack:
    #         return -1
    #     return self.stack[-1][0]

    # def getMin(self) -> int:
    #     if not self.stack:
    #         return float('inf')
    #     return self.stack[-1][1]
    
    # using two stacks
    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []    
    
    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.minStack or  self.minStack[-1] >= val: 
    #         self.minStack.append(val)

    # def pop(self) -> None:
    #     last_val = self.stack.pop()
    #     if last_val == self.minStack[-1]:
    #         self.minStack.pop()
        
    # def top(self) -> int:
    #     return self.stack[-1]
        
    # def getMin(self) -> int:
    #     return self.minStack[-1]
    
    #improved two stacks
    def __init__(self):
        self.stack = []
        self.minStack = []    
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1][0]:
            self.minStack.append((val, 1))
            return
        if val == self.minStack[-1][0]:
            min_val, n_times = self.minStack.pop()
            self.minStack.append((min_val, n_times + 1))

    def pop(self) -> None:
        last_val = self.stack.pop()
        if last_val == self.minStack[-1][0]:
            min_val, n_times = self.minStack.pop()
            n_times -= 1
            if n_times > 0:
                self.minStack.append((min_val, n_times))

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
