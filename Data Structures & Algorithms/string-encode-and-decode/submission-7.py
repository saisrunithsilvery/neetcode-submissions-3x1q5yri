class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""
        for word in strs:
            length = len(word)

            result += str(length) + "#" + word

        return result    

    def decode(self, s: str) -> List[str]:

        result = []
        r = 0
        while r < len(s):
            l = r
            while s[r] != "#":
                r +=1
            wrd_len = int(s[l:r])
            word = s[r + 1 : r + 1 + wrd_len]
            result.append(word)
            r += 1 + wrd_len
        return result    




