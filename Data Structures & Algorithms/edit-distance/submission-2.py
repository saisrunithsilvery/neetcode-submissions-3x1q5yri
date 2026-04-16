class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        memo = { }
        def solve(i, j):

            if (i, j) in memo:
                return memo[(i, j)]
                
            if i == m:
                return n - j

            if j == n:
                return m - i


            if word1[i] == word2[j]:
                memo[(i, j)]= solve(i+1, j+1)
                return memo[(i, j)]

            else:
               
                
                x = 1 + solve(i+1, j+1)
                y = 1+ solve(i+1,j)
                z = 1+ solve(i, j+1)
                memo[(i, j)] = min(x,y,z)    
                return memo[(i, j)]   
        return solve(0,0)        
