class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        directions = [(0,1), (0, -1), (1,0), (-1,0)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    queue.append((i,j))
                    
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in directions:
                            new_x = x + dx
                            new_y = y + dy
                            if isValid(new_x, new_y) and grid[new_x][new_y] == "1":
                                grid[new_x][new_y] = "0"
                                queue.append((new_x, new_y))
                    islands += 1
        
        return islands
                    
