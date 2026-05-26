class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = [0, 0, 0]

        for t in triplets:
            # Skip triplets that exceed any target value
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            # Merge by taking element-wise max
            merged[0] = max(merged[0], t[0])
            merged[1] = max(merged[1], t[1])
            merged[2] = max(merged[2], t[2])

        return merged == target