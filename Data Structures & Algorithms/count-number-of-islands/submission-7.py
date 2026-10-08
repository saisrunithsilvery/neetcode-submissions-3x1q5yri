class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0


        def dfs(row, col):

            grid[row][col] == "0"
            directions = [(0, 1), [1, 0], (-1, 0), (0, -1)]

            for ii, ij in directions:
                nr = row +ii
                nc = col +ij

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    dfs(nr, nc)  


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1':
                    result +=1
                    dfs(i, j)
        return result            
                    

        