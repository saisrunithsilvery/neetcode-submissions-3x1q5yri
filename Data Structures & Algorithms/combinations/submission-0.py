class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:



        subset = []
        result = []

        def solve(val):

            if val > n+1:
                return 

            if val == n+1 and len(subset) == k:
                result.append(subset.copy())
                return

            subset.append(val)
            solve(val+1)
            subset.pop()
            solve(val+1)   
            
        solve(1)
        return result    
        