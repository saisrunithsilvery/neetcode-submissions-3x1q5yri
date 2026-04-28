class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            # Out of bounds, already visited, or can't flow uphill
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or (r, c) in visited
                    or heights[r][c] < prev_height):
                return
            visited.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start DFS from Pacific borders (top row + left col)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])          # top row
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])          # left col

        # Start DFS from Atlantic borders (bottom row + right col)
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows-1][c])  # bottom row
        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols-1])   # right col

        # Intersection = cells that reach BOTH oceans
        return [[r, c] for r, c in pacific & atlantic]