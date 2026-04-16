class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        memo = {}

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            result = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    result = max(result, 1 + solve(ni, nj))
            
            memo[(i, j)] = result
            return result

        return max(solve(i, j) for i in range(m) for j in range(n))