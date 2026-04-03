
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {

            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        if not digits:
            return []

        part =[]
        sc = ""
        res =[]
        def dfs(i):
            if i == len(digits):
                res.append("".join(part))
                return


            for j in digitToChar[digits[i]]:

                part.append(j)
                dfs(i+1)
                part.pop()
        dfs(0)        
        return res


            