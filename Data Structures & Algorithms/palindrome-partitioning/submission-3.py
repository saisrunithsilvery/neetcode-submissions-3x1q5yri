class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        if not s:
            return []
        result = []
        part = []
        def ispali(i, j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i +=1
                j -=1
            return True            

        def dfs(i):

            if i == len(s):
                result.append(part.copy())

            for j in range(i, len(s)):

                if ispali(i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)            
        return result            






