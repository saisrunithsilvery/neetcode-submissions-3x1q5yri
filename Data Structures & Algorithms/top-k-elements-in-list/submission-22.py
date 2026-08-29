from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashset = {}

        for num in nums:
            hashset[num] = hashset.get(num, 0) + 1

        sorted_items = sorted(hashset.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in sorted_items[:k]]

        