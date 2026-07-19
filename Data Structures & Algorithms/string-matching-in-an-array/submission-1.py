class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        result = []
        words.sort(key = lambda x : len(x))
        print(words)
        for i in range(len(words)-1):
            len1 = len(words[i])
            for j in range(i+1, len(words)):

                for s in range(0, len(words[j])-len(words[i])+1):
                    if words[i]==words[j][s:len(words[i])+s]:
                        result.append(words[i])
        
        result = set(result)
        return list(result)
        