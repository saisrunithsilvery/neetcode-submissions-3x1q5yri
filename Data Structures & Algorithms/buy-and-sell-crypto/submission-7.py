class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0 
        buy = float('inf')
        

        for price in prices:

            if price < buy :
                buy = price

            else:
                result = max(result, price - buy)

        return result            

        