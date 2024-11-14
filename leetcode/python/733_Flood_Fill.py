class Solution:
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

        
