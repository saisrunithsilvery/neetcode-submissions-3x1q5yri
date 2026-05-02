class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        
        memo = [[-1]*amount for _ in range(0, n)]
        def solve(i, amt):
            if amt == amount:
                return 1

            if i >= n or amt > amount:
                return 0
            if memo[i][amt] != -1:
                return memo[i][amt]     


            x = solve(i, amt+coins[i])
            y = solve(i+1, amt) 
            
            memo[i][amt] = x+y
            return  memo[i][amt]
        return solve(0,0)
