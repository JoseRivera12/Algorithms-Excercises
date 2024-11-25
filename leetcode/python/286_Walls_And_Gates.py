class Solution:
    INF = 2147483647
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def isValid(x, y):
            return 0 <= x < rows and 0 <= y < cols
        """
        Do not return anything, modify rooms in-place instead.
        [[INF, -1,   0,   INF],
         [INF, INF,  INF, -1],
         [INF, -1,   INF, -1],
         [0,   -1,   INF, INF]]
        """
        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque()
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for x in range(rows):
            for y in range(cols):
                if rooms[x][y] == 0:
                    visited.add((x,y))
                    queue.append((x,y,0))
        
        
        while queue:
            x, y, steps = queue.popleft()
            for dx, dy in directions:
                next_x = x + dx
                next_y = y + dy
                if isValid(next_x, next_y) and rooms[next_x][next_y] == self.INF and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, steps + 1))
                    rooms[next_x][next_y] = steps + 1
        return rooms
            
                
