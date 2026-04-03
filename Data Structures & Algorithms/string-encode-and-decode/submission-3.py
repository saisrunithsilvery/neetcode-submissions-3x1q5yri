class Solution:

    
    def encode(self, strs: List[str]) -> str:
        output =""
        for strin in strs:
            x=len(strin)
            output += str(x)+"#"+strin
        return output    


    def decode(self, s: str) -> List[str]:

        i=0
        output =[]
        
        while i<len(s):

            j=i

            while s[j]!='#':
                j +=1
            length = int(s[i:j])
            output.append(s[j+1:j+1+length])
            i =1+length+j   
        
             
        return output