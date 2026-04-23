class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0 :
            return [0]
          
        res =[0,1]
       
        for x in range(2, n+1):

            a = x&(x-1)
            res.append(res[a]+1)
        return res    




        