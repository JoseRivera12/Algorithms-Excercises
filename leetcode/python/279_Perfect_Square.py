
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        if n in squares:
            return 1

        queue = deque([(n, 1)])
        visited = {n}

        while queue:
            remain, steps = queue.popleft()
            for square in squares:
                diff = remain - square
                
                if diff == 0:
                    return steps
                    
                if diff < 0:
                    break
                    
                if diff not in visited:
                    visited.add(diff)
                    queue.append((diff, steps + 1))
                    
        return -1
