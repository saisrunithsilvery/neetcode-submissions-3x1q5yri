from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxi_area = 0 
        visit = set()

        def bfs(i, j):
            nonlocal maxi_area

            q = deque()
            grid[i][j] = 0

            total = 1

            q.append([i, j])
            directions = [[0,1], [1, 0], [0, -1], [-1, 0]]

            while q:
                x, y = q.popleft()
                for ni, nj in directions :

                    if x+ni in range(0, len(grid)) and y+nj in range(0, len(grid[0])) and grid[x+ni][y+nj] == 1:
                        total +=1
                        grid[x+ni][y+nj] = 0
                        q.append((x+ni, y+nj))
            maxi_area = max(maxi_area, total)            







        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    bfs(i, j)

        return maxi_area            


        