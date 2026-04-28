from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pac = set()   # cells reachable by Pacific
        atl = set()   # cells reachable by Atlantic

        def bfs(starts):
            q = deque(starts)
            visited = set(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]):  # reverse: uphill
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited

        # Pacific starts: top row + left col
        pac_starts = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]

        # Atlantic starts: bottom row + right col
        atl_starts = [(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)]

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)

        # Cells in BOTH sets
        return [[r, c] for r, c in pac & atl]