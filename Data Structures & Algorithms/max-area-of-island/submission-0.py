class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        result = 0
        rows , cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):

            q = deque() 
            q.append((r, c))
            val = 1
            directions = [[-1, 0], [1,0], [0, 1], [0, -1] ]
            visit.add((r, c)) 

            while q:
                r, c = q.popleft()

                for dr, dc in directions:

                    if dr + r in range(rows) and dc + c in range(cols) and grid[dr + r][dc + c] == 1 and (dr + r, dc + c) not in visit :
                        val +=1
                        visit.add((dr + r, dc + c)) 
                        q.append((dr + r, dc + c))
            return val

  
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and (r, c) not in visit:

                    x = bfs(r, c)
                    result = max(result, x)

        return result






        
        