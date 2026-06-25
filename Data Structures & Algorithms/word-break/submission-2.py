class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        def solve(index):

            if index == len(s):
                return True
            
            for word in wordDict:

                if len(word)+ index -1 < len(s) and s[index:index+len(word)]== word:
                    if solve(index+len(word)):
                        return True
            return False            
        return solve(0)           





            

        