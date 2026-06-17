class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashmap = {}
        longest = -1

        for i, char in enumerate(s):

            if char not in hashmap:
                hashmap[char] = i
            else:

                longest = max(longest, i- hashmap[char] -1)

        return longest        





            

        