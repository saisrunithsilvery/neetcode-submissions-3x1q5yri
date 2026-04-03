class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        total = sum(nums)

        # If total is odd → cannot split equally
        if total % 2 != 0:
            return False

        target = total // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            temp=set()
            for p in dp:
                if p+nums[i]== target:
                    return True

                
                temp.add(p+nums[i])
                temp.add(nums[i])
            dp |= temp      

        return False            
