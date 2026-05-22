class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        
        candidates.sort()  # ← MUST sort first
        res = []
        subset = []
        def dt(sum1, i):
            if sum1 == target:
                res.append(subset.copy())
                return
            
            if sum1 > target or i >= len(candidates):
                return

            # Choice 1: INCLUDE candidates[i]
            subset.append(candidates[i])
            dt(sum1 + candidates[i], i + 1)
            subset.pop()
            # Choice 2: SKIP candidates[i] AND all its copies
             
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dt(sum1, i+1)  # ← jump past ALL copies

        dt( 0, 0)
        return res