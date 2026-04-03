class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        
        candidates.sort()  # ← MUST sort first
        res = []

        def dt(subset, sum1, i):
            if sum1 == target:
                res.append(subset)
                return
            
            if sum1 > target or i >= len(candidates):
                return

            # Choice 1: INCLUDE candidates[i]
            dt(subset + [candidates[i]], sum1 + candidates[i], i + 1)

            # Choice 2: SKIP candidates[i] AND all its copies
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dt(subset, sum1, j)  # ← jump past ALL copies

        dt([], 0, 0)
        return res