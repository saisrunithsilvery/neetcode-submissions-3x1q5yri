class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for word in strs:
            length = len(word)
            result += str(length)+ "#" + word

        return result    
            
    def decode(self, s: str) -> List[str]:

        l = 0
        result = []
        while l < len(s):
            r = l
            while s[r]!= "#":
                r +=1

            length = int(s[l:r])
            result.append(s[r+1:r+1+length])
            l = r +1+length
        return result    




