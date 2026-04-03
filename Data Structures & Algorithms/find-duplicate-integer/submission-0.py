class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: detect cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: find cycle entry (= duplicate)
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow