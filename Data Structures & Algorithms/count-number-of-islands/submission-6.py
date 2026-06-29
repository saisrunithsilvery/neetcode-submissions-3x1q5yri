class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()
        

        directions = [[1,0], [0,-1], [-1, 0], [0,1]]

        def bfs(i, j):
            q = deque()
            visit.add((i, j))
            q.append((i, j))
            while q:
                row, col = q.pop()
                for r, c in directions:
                    
                    if (0 <= row+r < len(grid) and
                    0 <= col+c < len(grid[0]) and
                    grid[row+r][col+c] == "1" and
                    (row+r, col+c) not in visit):

                        visit.add((row+r, col+c))
                        q.append((row+r, col+c))



        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1" and (i, j) not in visit:
                    count +=1
                    bfs(i,j)
        return count            
                
        