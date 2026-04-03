class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slidingwindow ={}
        count_t ={}
        res = [-1,-1]
        res_len=float('inf')
        for c in t:
            count_t[c]= count_t.get(c, 0) +1
        left =0
        have =0
        need = len(count_t)

        for right in range(len(s)):

            c=s[right]
            slidingwindow[c] = 1 + slidingwindow.get(c, 0)
            if c in count_t and slidingwindow[c] ==count_t[c]:
                have +=1

            while have == need:

                if (right - left+1) < res_len:
                    res =[left, right]
                    res_len = right -left +1
                slidingwindow[s[left]] -=1

                if s[left] in count_t and slidingwindow[s[left]]< count_t[s[left]]:
                    have -=1
                left +=1

        return s[res[0]:res[1]+1] if res_len != float('inf') else ''






        
        