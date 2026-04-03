class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # step 1: add ALL treasures to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # step 2: BFS outward from all treasures at once
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(rows) and nc in range(cols) 
                    and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))