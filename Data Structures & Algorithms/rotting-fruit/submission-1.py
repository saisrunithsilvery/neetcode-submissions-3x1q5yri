class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque


        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: collect all rotten fruits & count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        minutes = 0

        # Step 2: BFS level by level
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):      # process one full "minute"
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2      # mark rotten
                        fresh -= 1
                        queue.append((nr, nc))

        # Step 3: any fresh left?
        return minutes if fresh == 0 else -1