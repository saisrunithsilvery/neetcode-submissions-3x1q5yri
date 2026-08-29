class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        set1 = set()

        for val in nums :
            if val in set1:
                return True
            set1.add(val)    
        return False
