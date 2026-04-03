class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x= set()
        for i in nums:
            if i not in x:
                x.add(i)
            else:
                return True
        return False             
        