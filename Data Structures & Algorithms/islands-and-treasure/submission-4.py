from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()
        directions = [[1,0], [0,-1], [-1, 0], [0,1]]
        visit =set()

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):

                if grid[i][j] == 0:
                    q.append((0, i, j))

        while q:

            val, x, y = q.popleft()

            for i, j in directions:
                ni, nj = x+i, y+j

                if ni in range(0, len(grid)) and nj in range(0, len(grid[0])) and grid[ni][nj] == 2147483647 and (ni, nj) not in visit :
                    grid[ni][nj] = val+1
                    q.append((val+1, ni, nj))
                    visit.add((ni, nj))








        