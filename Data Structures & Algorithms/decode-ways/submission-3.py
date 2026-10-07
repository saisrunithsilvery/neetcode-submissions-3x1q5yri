class Solution:
    def numDecodings(self, s: str) -> int:

        
        memo = {}
       
        def dfs(index):
            total = 0

            if index in memo:
                return memo[index]
            if index == len(s):
                return 1 

            val1 = int(s[index:index+1])
            val2 = int(s[index: index+2])

            if 0 < val1 < 10:
                total += dfs(index+1)

            if 10 <= val2 <= 26:
                total +=  dfs(index+2)

            memo[index] = total
            return total
        return dfs(0)    

        