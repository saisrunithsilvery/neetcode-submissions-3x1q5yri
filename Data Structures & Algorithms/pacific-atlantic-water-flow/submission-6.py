from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []
        
        atlantic_visit = set()
        pacific_visit = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(row, col, visit):
            if (row, col) in visit:
                return
            visit.add((row, col))
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dr, col + dc    
               
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if heights[new_row][new_col] >= heights[row][col]:
                        dfs(new_row, new_col, visit)
  
        for i in range(rows):
            dfs(i, 0, pacific_visit)  
            dfs(i, cols - 1, atlantic_visit)

        for j in range(cols):
            dfs(0, j, pacific_visit) 
            dfs(rows - 1, j, atlantic_visit)   

                   
        return list(pacific_visit & atlantic_visit)

