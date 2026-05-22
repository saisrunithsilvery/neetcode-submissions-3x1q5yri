class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(i, subset, remaining):
            # ✓ Base case: found solution
            if remaining == 0:
                res.append(subset[:])
                return
            
            # ✓ Pruning: Can't reach target even if we take all remaining
            if i >= len(candidates) or candidates[i] > remaining:
                return
            
            for j in range(i, len(candidates)):
                # ✓ Skip duplicates
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                # ✓ Pruning: Stop if current element already too large
                if candidates[j] > remaining:
                    break
                
                subset.append(candidates[j])
                backtrack(j + 1, subset, remaining - candidates[j])
                subset.pop()
        
        backtrack(0, [], target)
        return res