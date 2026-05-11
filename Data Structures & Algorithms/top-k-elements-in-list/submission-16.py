
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse = True)
        res={}
       
        for i in nums:
            if i in res:
                res[i] +=1
            else:
                res[i] =1
        x=sorted(res.keys(), key=lambda x: res[x], reverse=True)
        return x[:k]       
        

        