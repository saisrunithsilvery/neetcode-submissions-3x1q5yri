class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):  # j starts at i, moves right
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        return count