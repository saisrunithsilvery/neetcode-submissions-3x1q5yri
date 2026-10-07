class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        def solve(index, total):

            if total == amount :
                return 0
            if total > amount or index == n:
                return float('inf')    

            x = 1 + solve(index, total+coins[index])
            y = solve(index+1, total)
            
            
            return min(x, y)
        return solve(0, 0) if solve(0,0) != float('inf') else -1






        