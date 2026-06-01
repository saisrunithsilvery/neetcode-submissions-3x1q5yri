class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1

        # Sort by frequency (value), not by key, in descending order
        x = sorted(dict1.keys(), key=lambda a: dict1[a], reverse=True)
        
        return x[:k]