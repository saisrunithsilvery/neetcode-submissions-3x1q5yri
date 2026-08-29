class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False

        hashset = {}

        for letter in s:

            if letter not in hashset:
                hashset[letter] = 0
            hashset[letter] +=1
        
        for letter in t:

            if letter not in hashset:
                return False
            hashset[letter] -=1
            if hashset[letter] < 0:
                return False
        return True        

                


                    
        