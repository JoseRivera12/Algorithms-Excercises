cclass Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         def isValid(row, col):
#             return 0 <= row < rows and 0 <= col < cols
        
#         def dfs(row, col, init_color):
#             if not isValid(row, col) or image[row][col] != init_color:
#                 return
            
#             image[row][col] = color
            
#             dfs(row, col + 1,init_color)
#             dfs(row, col - 1,init_color)
#             dfs(row - 1, col,init_color)
#             dfs(row + 1, col,init_color)
        
#         rows = len(image)
#         cols = len(image[0])
        
#         init_color = image[sr][sc]
#         if init_color != color:
#             dfs(sr, sc, init_color)
        
#         return image
        def isValid(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        init_color = image[sr][sc]
        if init_color == color:
            return image
        
        rows = len(image)
        cols = len(image[0])
        queue = deque()
        visited = set()
        
        queue.append((sr, sc))
        visited.add((sr, sc))
        directions = [(0,-1), (0, 1), (-1,0),(1,0)]
        
        while queue:
            x, y = queue.popleft()
            image[x][y] = color
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if isValid(new_x, new_y) and image[new_x][new_y] == init_color:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        
        return image
        
        
          
        lass Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # initial approach
        # def fill(row: int, col: int, start: int):
        #     if image[row][col] != start:
        #         return
        #     image[row][col] = color
        #     if row - 1 >= 0:
        #         fill(row - 1, col, start)
        #     if row + 1 < rows:
        #         fill(row + 1, col, start)
        #     if col + 1 < cols:
        #         fill(row, col + 1, start)
        #     if col - 1 >= 0:
        #         fill(row, col - 1, start)
            
        
        # rows = len(image)
        # cols = len(image[0])

        # start = image[sr][sc]
        # if start != color:
        #     fill(sr, sc, start)
        # return image
            start = image[sr][sc]
            if start == color:  # Avoid infinite recursion if start color equals target color
                return image
                
            rows = len(image)
            cols = len(image[0])
            
            def fill(row: int, col: int):
                if (row < 0 or row >= rows or 
                    col < 0 or col >= cols or 
                    image[row][col] != start):
                    return
                    
                image[row][col] = color
                
                # Check all 4 directions
                fill(row - 1, col)  
                fill(row + 1, col)
                fill(row, col - 1)
                fill(row, col + 1)
            
            fill(sr, sc)
            return image

        
