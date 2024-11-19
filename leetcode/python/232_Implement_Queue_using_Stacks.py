class MyQueue:
    # first approach
    # def __init__(self):
    #     self.stack = []
    #     self._aux = []

    # def push(self, x: int) -> None:
    #     while self.stack:
    #         self._aux.append(self.stack.pop())
        
    #     self._aux.append(x)
        
    #     while self._aux:
    #         self.stack.append(self._aux.pop())

    # def pop(self) -> int:
    #     if not self.empty():
    #         return self.stack.pop()

    # def peek(self) -> int:
    #     return self.stack[-1]

    # def empty(self) -> bool:
    #     return len(self.stack) == 0
    
    # amortized approach
    def __init__(self):
        self.stack = []
        self._aux = []
        self._front = -1

    def push(self, x: int) -> None:
        if not self.stack:
            self._front = x
        self.stack.append(x)
            
    def pop(self) -> int:
        if not self._aux:
            while self.stack:
                self._aux.append(self.stack.pop())
        return self._aux.pop()

    def peek(self) -> int:
        if self._aux:
            return self._aux[-1]
        return self._front

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self._aux) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
