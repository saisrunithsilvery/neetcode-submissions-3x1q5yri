class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset =[]
        sum1 =0
        res =[]
        i = 0
        def dt(subset, sum1, i):

            if i >= len(nums):
                return

            if sum1 > target:
                return

            elif sum1 == target:
                res.append(subset)
                return

           
            dt(subset + [nums[i]], sum1 + nums[i], i )
            dt(subset, sum1, i+1)

        dt(subset, sum1, i)  

        return res  
           

                    
                    

        