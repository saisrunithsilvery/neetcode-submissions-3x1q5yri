class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        result = 0
        def solve(i, amt):

            if i >= n or amt > amount:
                return 0 

            if amt == amount:
                return 1

            x = solve(i, amt+coins[i])
            y = solve(i+1, amt) 
            
            result = x+y
            return  result 
        return solve(0,0)
