class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashset = defaultdict(list)
        

        for word in strs:
            letters = [0]*26
            for char in word:

                index = ord(char)-ord('a')
                letters[index] +=1
            hashset[(tuple(letters))].append(word) 

        return list(hashset.values() )   

