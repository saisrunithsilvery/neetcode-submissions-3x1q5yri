from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])

        # top and bottom rows
        for i in range(cols):
            pacific.add((0, i))
            atlantic.add((rows - 1, i))

        # left and right columns
        for j in range(rows):
            pacific.add((j, 0))
            atlantic.add((j, cols - 1))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def bfs(visited):

            q = deque(visited)

            while q:

                r, c = q.popleft()

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):

                        visited.add((nr, nc))
                        q.append((nr, nc))

        bfs(pacific)
        bfs(atlantic)

        result = []

        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])

        return result