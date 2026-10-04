class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        result = []
        subset = []
        candidates.sort()

        def solve(index, total):

            if target == total:
                result.append(subset.copy())
                return

            if target < total or len(candidates)== index:
                return           

            #Include
            subset.append(candidates[index])
            solve(index+1, total+candidates[index])
            subset.pop()


            # Exclude candidates[index] AND all its duplicates
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            solve(index + 1, total)

        solve(0, 0)
        return result


