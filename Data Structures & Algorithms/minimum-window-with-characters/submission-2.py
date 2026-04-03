
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = {}
        t_dic ={}

        for i in range(len(t)):
            t_dic[t[i]]=t_dic.get(t[i],0)+1
        need = len(t_dic)
        have =0
        left =0
        res_len =float('inf')
        res = [-1, -1]


        for right in range(len(s)):
            ch =s[right]
            output[s[right]] = output.get(s[right],0)+1

            if ch in t_dic and t_dic[ch] ==output[ch]:
                    have +=1
                

            while need == have:
                if (right - left +1) < res_len:
                    res =[left, right]
                    res_len = right -left +1

                y=s[left]    
                output[y] -=1
                if y in t_dic and output[y]<t_dic[y]:
                    have -=1

                left +=1
        L, R = res
        return "" if res_len ==float("inf") else s[L:R+1]







        
        