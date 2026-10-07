class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == "0":
            return 0

        n = len(s)
        
        dp = [0]*(n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1 ):


            if 0 < int(s[i]) < 10 :

                dp[i] += dp[i+1]

            if i+1 < len(s):
                dp [i] += dp[i+2]  
        return dp[0]          

            
        


       
        

        