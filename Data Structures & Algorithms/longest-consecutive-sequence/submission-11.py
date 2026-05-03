class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x=set(nums)
        res=0
        for i in nums:
            if i-1 not in x:
                longest =1
                curr = i
                while curr+1 in x:
                    curr +=1
                    longest +=1
                
                res = max(longest,res)
        return res        

