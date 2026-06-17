class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        count = 0
        odd = 0
        for i in s:
            hashmap[i] = hashmap.get(i, 0)+1

        
        for i in hashmap.values():

            if i%2 == 0:
                count += i
            else:
                
                count += i-1
                odd = 1

        if odd == 1:
            return count +1
        else:
            return count            

