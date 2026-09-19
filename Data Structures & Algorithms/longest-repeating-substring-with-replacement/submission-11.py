class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        str_len = len(s)
        hashset = {}
        result = 0
        while r < str_len :

            hashset[s[r]] = hashset.get(s[r], 0) +1
            largest = max(hashset.values())

            while r-l+1 > largest + k :
                hashset[s[l]] -=1
                l +=1

            result = max(result, r-l+1) 
            r +=1

        return result       





