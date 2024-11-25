class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.curr_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        self.curr_sum += val - tail
        return self.curr_sum / min(self.size, self.count)
        
