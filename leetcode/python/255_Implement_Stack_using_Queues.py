class MyStack:
    # two queues push O(n) pop O(1)
    # def __init__(self):
    #     self.flag = False
    #     self.queue = deque()
    #     self.aux_queue = deque()
        

    # def push(self, x: int) -> None:
    #     if not self.queue:
    #         self.queue.append(x)
    #     else:
    #         self.aux_queue.append(x)
        
    #     if self.queue and self.aux_queue:
    #         if not self.flag:
    #             while self.queue:
    #                 self.aux_queue.append(self.queue.popleft())
    #             self.flag = True
    #         else:
    #             while self.aux_queue:
    #                 self.queue.append(self.aux_queue.popleft())
    #             self.flag = False
        
    # def pop(self) -> int:
    #     if not self.queue:
    #         return self.aux_queue.popleft()
    #     else:
    #         return self.queue.popleft()

    # def top(self) -> int:
    #     if not self.queue:
    #         return self.aux_queue[0]
    #     else:
    #         return self.queue[0]   

    # def empty(self) -> bool:
    #     return not self.queue and not self.aux_queue
    
    def __init__(self):
        self.queue = deque()
    
    def push(self, x: int) -> None:
        self.queue.append(x)
        i = len(self.queue)
        while i > 1:
            self.queue.append(self.queue.popleft())
            i -= 1

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
