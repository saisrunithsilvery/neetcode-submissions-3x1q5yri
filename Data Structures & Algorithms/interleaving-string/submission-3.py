class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}

        def solve(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            if i < len(s1) and j < len(s2) and s1[i] == s3[i+j] and s2[j] == s3[i+j]:
                memo[(i, j)] = solve(i+1, j) or solve(i, j+1)

            elif i < len(s1) and s1[i] == s3[i+j]:
                memo[(i, j)] = solve(i+1, j)

            elif j < len(s2) and s2[j] == s3[i+j]:
                memo[(i, j)] = solve(i, j+1)

            else:
                memo[(i, j)] = False

            return memo[(i, j)]

        return solve(0, 0)