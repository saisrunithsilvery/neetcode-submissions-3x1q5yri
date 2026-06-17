class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        hashmap = {}

        


        for word in words:
            for char in word:
                hashmap[char] = hashmap.get(char, 0)+1


        for val in hashmap.values() :
            if val % len(words) != 0:
                return False
        return True        

 

        