class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        def solve(index, total):

            if (index, total) in memo:
                return memo[(index, total)] 

            if total == amount :
                return 0

            if total > amount or index == n:
                return float('inf')    

            x = 1 + solve(index, total+coins[index])
            y = solve(index+1, total)
            
            
            memo[(index, total)] = min(x, y)
            return memo[(index, total)]
        return solve(0, 0) if solve(0,0) != float('inf') else -1






        