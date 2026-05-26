class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_map = {0: 1}  # Track prefix sums
        
        for num in nums:
            prefix_sum += num
            # If (prefix_sum - k) exists, we found valid subarrays
            if prefix_sum - k in sum_map:
                count += sum_map[prefix_sum - k]
            sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1
        
        return count