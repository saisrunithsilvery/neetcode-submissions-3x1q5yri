class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n1 = len(s)
        n2 = len(t)

        count_s1 = {}
        count_s2 = {}

        res = [-1, -1]
        res_len = float('inf')

        have = 0

        left = 0

        for i in t :
            count_s1[i] = count_s1.get(i, 0) +1

        need = len(count_s1) 

        for r in range(len(s)):

            count_s2[s[r]] = count_s2.get(s[r], 0) + 1
            if s[r] in count_s1 and count_s2[s[r]] == count_s1[s[r]]:
                have +=1

            while need == have :
                if r - left +1 < res_len :
                    res = [left, r]
                    res_len = r - left +1
                
                if s[left] in count_s1 and count_s1[s[left]] == count_s2[s[left]]:
                    count_s2[s[left]] -= 1
                    have -=1
                left +=1

        return s[res[0]: res[1]+1]            

