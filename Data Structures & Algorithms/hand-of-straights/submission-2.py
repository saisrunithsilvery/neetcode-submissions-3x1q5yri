class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        dic = {}

        if len(hand) % groupSize != 0 :
            return False

        for i in hand:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1

        for  i in range(0, len(hand)// groupSize):

            x = min(dic.keys())

            for j in range(0, groupSize):
                
                if x in dic and dic[x] > 0:
                    dic[x] -=1
                    if dic[x] == 0:
                        dic.pop(x)
                    x +=1    


                else:
                    return False
        return True            

                            
        